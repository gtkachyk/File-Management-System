from Model.instance import Instance

# Notes:
# - Methods in this class are those that require access to the Global directory
# - The Archive instance does not require Backup-Storage and thus capacity.
class Controller (Instance):
    def __init__(self, name, capacity, Save=None, BackupStorage=None, standard_instances=None):
        super().__init__(name, capacity, Save=Save, BackupStorage=BackupStorage)
        self.Global = []
        self.add_instance(Instance('Archive', 0, self, Save=[]))
        self.add_instance(self)
        self.refresh()
    

    def refresh (self):
        self.sort_network()
        self.set_base_copy()


    def add_instance (self, instance):
        self.Global.append(instance)
        self.refresh()


    def add_instances (self, instances):
        self.Global += instances
        self.refresh()


    def removed_stale_files (self, instance):
        system_data = self.get_system_data()
        for folder in instance.BackupStorage:
            if folder not in system_data:
                instance.remove_from_backupstorage(folder)


    def confirm_network_state (network, save_directories, backup_storage_directories, copies):
        i = 0
        for i in range(len(network)):
            if len(network[i].Save) != len(save_directories[i]):
                print("The Save directory of instance " + network[i].name + " is " + str(network[i].Save) + ", but its expected value was " + str(save_directories[i]))
                return False
            if len(network[i].BackupStorage) != len(backup_storage_directories[i]):
                print("The BackupStorage directory of instance " + network[i].name + " is " + str(network[i].BackupStorage) + ", but its expected value was " + str(backup_storage_directories[i]))
                return False
            for folder in network[i].Save:
                if folder not in save_directories[i]:
                    print("The Save directory of instance " + network[i].name + " is " + str(network[i].Save) + ", but its expected value was " + str(save_directories[i]))
                    return False
            for folder in save_directories[i]:
                if folder not in network[i].Save:
                    print("The Save directory of instance " + network[i].name + " is " + str(network[i].Save) + ", but its expected value was " + str(save_directories[i]))
                    return False
            for folder in network[i].BackupStorage:
                if folder not in backup_storage_directories[i]:
                    print("The BackupStorage directory of instance " + network[i].name + " is " + str(network[i].BackupStorage) + ", but its expected value was " + str(backup_storage_directories[i]))
                    return False
            for folder in backup_storage_directories[i]:
                if folder not in network[i].BackupStorage:
                    print("The BackupStorage directory of instance " + network[i].name + " is " + str(network[i].BackupStorage) + ", but its expected value was " + str(backup_storage_directories[i]))
                    return False
            if isinstance(network[i], Controller):
                for copy in network[i].get_copies():
                    if not copy in copies:
                        print("The copies of the network with controller " + network[i].name + " are " + str(network[i].get_copies()) + ", but the expected copies were " + str(copies))
                        return False
                for copy in copies:
                    if not copy in network[i].get_copies():
                        print("The copies of the network with controller " + network[i].name + " are " + str(network[i].get_copies()) + ", but the expected copies were " + str(copies))
                        return False
            i += 1
        return True


    # The official order of instances in a network
    def sort_network (self):
        for n in range(len(self.Global) - 1, 0, -1):
            swapped = False  
            for i in range(n):
                if self.Global[i].capacity > self.Global[i + 1].capacity:
                    self.Global[i], self.Global[i + 1] = self.Global[i + 1], self.Global[i]
                    swapped = True

            if not swapped:
                break


    def print_network (self):
        for instance in self.Global:
            Instance.print_instance(instance)


    def get_unique_copy_id (self):
        copy_ids = []
        for instance in self.Global:
            copy_ids.append(instance.copy_id)
        
        unique_id = 0
        while unique_id in copy_ids:
            unique_id += 1
        
        return unique_id

    
    def get_system_data (self):
        system_data = []
        for instance in self.Global:
            for folder in instance.Save:
                system_data.append(folder)
        return system_data
    

    def get_copies (self):
        copies = {}
        for instance in self.Global:
            if instance.has_copy_id():
                if instance.copy_id in copies:
                    copies[instance.copy_id].append(instance.name)
                else:
                    copies.setdefault(instance.copy_id, [])
                    copies[instance.copy_id].append(instance.name)
        return copies
                

    # Note that if an instance is eligible to add a partial copy, it is eligible for addition
    def is_partial_copy_eligible (self, instance):
        if not len(self.get_system_data()) == 0 and not self.can_store_full_copy(instance) and instance.get_remaining_capacity() > 0 and not instance.has_copy_id():
            return True
        return False


    # Note that if an instance is eligible to add a full copy, it is eligible for addition
    def is_full_copy_eligible (self, instance):
        if not len(self.get_system_data()) == 0 and not self.stores_full_copy(instance) and self.can_store_full_copy(instance):
            return True
        return False


    # An instance can store a full copy if its capacity is greater than or equal to the size of system data minus the size of system data files it stores in its Save folder
    def can_store_full_copy (self, instance):
        return instance.capacity >= (len(self.get_system_data()) - len(instance.Save))
    

    # Algorithm for checking if an instance I has a unique copy id
    def has_unique_copy_id (self, instance):
        # If I does not have a copy id, then it does not have a unique copy id
        if not instance.has_copy_id():
            return False
        
        # Otherwise, go to the Global directory on the controller of I and check if any other instance has the same copy id as I
        for i in self.Global:
            if i.name != instance.name and i.copy_id == instance.copy_id:
                return False
        return True


    def get_incomplete_copy (self):
        system_data = self.get_system_data()
        for copy_id in self.get_copies().keys():
            for file in system_data:
                if file not in self.get_copy_files(copy_id):
                    return copy_id
        return -1
    

    # Precondition: I must be partial copy eligible
    def add_partial_copy (self, instance):
        system_data = self.get_system_data()
        incomplete_copy_id = self.get_incomplete_copy()
        if incomplete_copy_id == -1:
            # Start new copy
            i = 0
            while i < len(system_data) and instance.get_remaining_capacity != 0:
                if self.can_add_to_backupstorage(system_data[i], instance): self.add_to_backupstorage(system_data[i], instance)
                i += 1
            instance.copy_id = self.get_unique_copy_id()
        else:
            # Continue incomplete copy
            added_folder = False
            for file in system_data:
                if file not in self.get_copy_files(incomplete_copy_id) and instance.get_remaining_capacity != 0:
                    if self.can_add_to_backupstorage(file, instance):
                        self.add_to_backupstorage(file, instance)
                        added_folder = True
            if added_folder: instance.copy_id = incomplete_copy_id


    # Algorithm for adding a full copy of system data to an instance I.
    # Precondition: I must be full copy eligible
    def add_full_copy (self, instance):
        # Clear Backup-Storage
        instance.BackupStorage = []

        # Add the following files to the Backup-Storage directory of I:
        # - System data files that are not already in the Backup-Storage directory of I
        # - System data files that are not already in the Save directory of 
        for file in self.get_system_data():
            if self.can_add_to_backupstorage(file, instance): self.add_to_backupstorage(file, instance)

        # After, if I does not have a unique copy id, give it one
        if not self.has_unique_copy_id(instance): instance.copy_id = self.get_unique_copy_id()


    # Get files that can be added to the Backup-Storage folder of an instance
    def get_eligible_files (self, instance):
        files = []
        system_data = self.get_system_data()
        for file in system_data:
            if file not in instance.BackupStorage and file not in instance.Save:
                files.append(file)
        return files


    # Get all files stored in a copy
    def get_copy_files (self, id):
        if id == -1: return []
        system_data = self.get_system_data()
        files = []
        for instance in self.Global:
            if instance.copy_id == id:
                for file in instance.BackupStorage:
                    if file in system_data: files.append(file)
                for file in instance.Save:
                    files.append(file)
        return files


    def sort_folders (self, folders):
        output = folders
        for n in range(len(output) - 1, 0, -1):
            swapped = False  
            for i in range(n):
                if output[i] > output[i + 1]:
                    output[i], output[i + 1] = output[i + 1], output[i]
                    swapped = True

            if not swapped:
                break

        return output
    

    def sort_group (self, group):
        output = group
        for n in range(len(output) - 1, 0, -1):
            swapped = False  
            for i in range(n):
                if output[i][0] > output[i + 1][0]:
                    output[i], output[i + 1] = output[i + 1], output[i]
                    swapped = True

            if not swapped:
                break

        return output


    def sort_frequencies (self, frequencies):
        # print("Input = " + str(frequencies))
        sorted = []
        for key in frequencies:
            sorted.append([key, frequencies[key]])
        for n in range(len(sorted) - 1, 0, -1):
            swapped = False  
            for i in range(n):
                if sorted[i][1] > sorted[i + 1][1]:
                    sorted[i], sorted[i + 1] = sorted[i + 1], sorted[i]
                    swapped = True

            if not swapped:
                break
        groups = []
        group = []
        current = sorted[0][1]
        for i in range(len(sorted)):
            if sorted[i][1] == current:
                group.append(sorted[i])
            else:
                current = sorted[i][1]
                groups.append(self.sort_group(group))
                group = []
                group.append(sorted[i])

        # print("Groups = " + str(groups))

        output = []
        for i in range(len(sorted)):
            output.append(sorted[i][0])

        # print("Output = " + str(output))
        return output


    def get_frequencies (self, files):
        frequencies = {}
        for file in files:
            if file in frequencies:
                frequencies[file] += 1
            else:
                frequencies.setdefault(file, 1)

        sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1])
        {k: v for k, v in sorted_frequencies}
        print(sorted_frequencies)

        output_2 = []
        group = []
        current = None
        for pair in sorted_frequencies:
            if current == None: current = list(pair)[1]
            if list(pair)[1] == current:
                group.append(list(pair))
            else:
                sorted_group = self.sort_group(group)
                for i in sorted_group:
                    output_2.append(i[0])
                group = [list(pair)]
                current = list(pair)[1]
        if len(group) != 0:
            sorted_group = self.sort_group(group)
            for i in sorted_group:
                output_2.append(i[0])
        return output_2


    # An algorithm for using unused space in an instance I that stores part of a copy
    # Preconditions: I is not partial copy eligible or full copy eligible
    def add_to_partial_copy (self, instance):
        # Get system data files this instance does not contain
        eligible_files = self.get_eligible_files(instance)
        
        # Get list of files in the copy, create hashmap with key value pairs file:frequency, sort the hashmap in ascending order of frequency
        copy_files = self.sort_folders(self.get_copy_files(instance.copy_id))
        keys = self.get_frequencies(copy_files)

        # If any system data files are not in keys, add them to the front
        files = []
        for file in self.get_system_data():
            if file not in keys:
                files.append(file)
        files = self.sort_folders(files)
        files += keys

        # if True: print("For instance " + instance.name + ":\neligible_files = " + str(eligible_files) + "\ncopy_files = " + str(copy_files) + "\nkeys = " + str(keys) + "\nfiles = " + str(files))
        # For each pair in the hashmap, add the key (file) to instance if it is an eligible file and instance has space
        for file in files:
            if instance.get_remaining_capacity() > 0 and file in eligible_files:
                if self.can_add_to_backupstorage(file, instance): self.add_to_backupstorage(file, instance)


    # Note that if an instance is eligible to add files, it doesn't mean it is eligible to add a partial copy or full copy
    def is_eligible_for_addition (self, instance):
        if not len(self.get_system_data()) == 0 and not self.stores_full_copy(instance) and instance.get_remaining_capacity() > 0:
            return True
        return False


    def fill_unused_instance_space (self, instance):
        if self.is_partial_copy_eligible(instance):
            self.add_partial_copy(instance)
        elif self.is_full_copy_eligible(instance):
            self.add_full_copy(instance)
        elif self.is_eligible_for_addition(instance):
            self.add_to_partial_copy(instance)
        else:
            # print("Instance " + instance.name + " has no usable space.")
            pass


    def fill_unused_network_space (self):
        for instance in self.Global:
            self.fill_unused_instance_space(instance)


    def stores_full_copy (self, instance):
        system_data = self.get_system_data()
        for file in system_data:
            if file not in instance.BackupStorage and file not in instance.Save:
                return False
        return True
    

    # An instance is a breakaway copy if it stores a full copy of system data split between its Save and Backup-Storage directory
    def is_breakaway_copy (self, instance):
        if self.stores_full_copy(instance) and len(instance.Save) != 0 and len(instance.BackupStorage) != 0:
            return True
        return False
    

    # An instance is part of the base copy if it contains system data and is not a breakaway copy
    def is_base_copy_part (self, instance):
        if instance.contains_system_data() and not self.is_breakaway_copy(instance):
            return True
        return False


    def set_base_copy (self):
        for instance in self.Global:
            if self.is_base_copy_part(instance):
                instance.copy_id = -1
        
        copy_id = self.get_unique_copy_id()
        for instance in self.Global:
            if self.is_base_copy_part(instance):
                instance.copy_id = copy_id


    # To add a folder F to the Backup-Storage directory of an instance I, the following conditions must be satisfied:
    # - I must have enough remaining capacity to store F
    # - F must not be in the Save or Backup-Storage directory of I
    # - F must be in system data
    def can_add_to_backupstorage (self, folder, instance):
        if instance.get_remaining_capacity() >= 1 and folder not in instance.Save and folder not in instance.BackupStorage and folder in self.get_system_data():
            return True
        return False


    # The official algorithm for adding folders to Backup-Storage
    # Precondition: all files in file_data must be eligible to be added to the Backup-Storage directory of instance
    # Note that a file does not have to be eligible to be stored in the Backup-Storage directory of an instance to be in the Backup-Storage directory of that instance.
    # This is because some ineligible files might be present after files are removed from a network's system data
    def add_to_backupstorage (self, file_data, instance):
        if type(file_data) is int:
            instance.BackupStorage.append(file_data)
        elif type(file_data) is list:
            for file in file_data:
                instance.BackupStorage.append(file)
        else:
            raise ValueError('file_data must be and int or list')
    

    def get_stale_folders (self, instance):
        stale_folders = []
        system_data = self.get_system_data()
        for folder in instance.BackupStorage:
            if folder not in system_data:
                stale_folders.append(folder)
        return stale_folders

        