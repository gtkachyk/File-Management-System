# Notes:
# - The Storage-Extension directory is not needed in this model as is does not require any special algorithms to manage.
class Instance:
    def __init__(self, name, capacity, controller=None, Save=None, BackupStorage=None):
        self.name = name

        # The capacity integer represents number of system data folders this instance can store in Backup-Storage
        self.capacity = capacity
        self.controller = controller if controller is not None else None

        # Each integer in Save represents a folder with a shortcut in the File-Management-System/Save directory of this instance
        self.Save = Save if Save is not None else []

        # Each integer in BackupStorage represents a system data folder that is correctly stored in the Backup-Storage directory of this instance
        self.BackupStorage = BackupStorage if BackupStorage is not None else []
        self.copy_id = -1
    

    def contains_system_data (self):
        if self.Save == None: return False
        return len(self.Save) > 0
    

    def print_instance (self):
        print("Instance " + self.name + ":")
        print("    Capacity: " + str(self.capacity))
        print("    File-Management-System/Save: " + str(self.Save))
        print("    Backup-Storage: " + str(self.BackupStorage))
        print("    Copy ID: " + str(self.copy_id))


    def get_remaining_capacity (self):
        return self.capacity - len(self.BackupStorage)
    

    def add_to_save (self, folder_data):
        if type(folder_data) is int:
            self.Save.append(folder_data)
        elif type(folder_data) is list:
            self.Save += folder_data
        else:
            raise ValueError('folder_data must be and int or list')
        

    def remove_from_save (self, folder_data):
        if type(folder_data) is int:
            self.Save.remove(folder_data)
        elif type(folder_data) is list:
            for file in folder_data:
                self.Save.remove(file)
        else:
            raise ValueError('folder_data must be and int or list')


    def remove_from_backupstorage (self, folder_data=None):
        if folder_data == None:
            self.BackupStorage.pop()
        elif type(folder_data) is int:
            self.BackupStorage.remove(folder_data)
        elif type(folder_data) is list:
            for folder in folder_data:
                self.BackupStorage.remove(folder)
        else:
            raise ValueError('folder_data must be and int or list')
        if len(self.BackupStorage) == 0:
            self.copy_id = -1


    def get_controller (self):
        return self if self.controller is None else self.controller
    

    def has_copy_id (self):
        return not self.copy_id == -1
    

    def set_capacity (self, new_capacity):
        self.capacity = new_capacity
        while len(self.BackupStorage) > new_capacity:
            self.remove_from_backupstorage()

