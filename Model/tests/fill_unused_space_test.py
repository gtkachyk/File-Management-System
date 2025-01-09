import unittest
from Model.instance import Instance
from Model.controller import Controller

class FillUnusedSpaceTest (unittest.TestCase):

    Controller_Instance_Laptop = None
    Standard_Instance_USB = None
    Standard_Instance_Phone = None
    Standard_Instance_Desktop = None
    Standard_Instance_HDD = None
    Standard_Instance_Tablet = None
    
    @classmethod
    def setUpClass (cls):
        # This is where the virtual archive instance is created
        cls.Controller_Instance_Laptop = Controller("Laptop", 0, [1, 2, 3], [])
        cls.Standard_Instance_USB = Instance("USB", 3, cls.Controller_Instance_Laptop, [], [])
        cls.Standard_Instance_Phone = Instance("Phone", 5, cls.Controller_Instance_Laptop, [4, 5], [])
        cls.Standard_Instance_Desktop = Instance("Desktop", 8, cls.Controller_Instance_Laptop, [6, 7, 8, 9, 10], [])
        cls.Standard_Instance_HDD = Instance("HDD", 10, cls.Controller_Instance_Laptop, [], [])
        cls.Standard_Instance_Tablet = Instance("Tablet", 5)

        cls.Controller_Instance_Laptop.add_instances([cls.Standard_Instance_USB, cls.Standard_Instance_Phone, cls.Standard_Instance_Desktop, cls.Standard_Instance_HDD])

    @classmethod
    def tearDownClass (cls):
        # This is where the virtual archive instance is deleted
        cls.Controller_Instance_Laptop = None
        cls.Standard_Instance_USB = None
        cls.Standard_Instance_Phone = None
        cls.Standard_Instance_Desktop = None
        cls.Standard_Instance_HDD = None
        cls.Standard_Instance_Tablet = None

    def test_01_initial (self):
        self.Controller_Instance_Laptop.fill_unused_network_space()

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD], 
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], []], 
                                                         backup_storage_directories=[[], [1, 2, 3], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone"], 1:["USB"], 2:["Desktop"], 3:["HDD"]}))
    
    def test_02_increase_capacity_1 (self):
        self.Standard_Instance_USB.set_capacity(5)
        self.Controller_Instance_Laptop.fill_unused_instance_space(self.Standard_Instance_USB)

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD],
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], []], 
                                                         backup_storage_directories=[[], [1, 2, 3, 4, 5], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone"], 1:["USB"], 2:["Desktop"], 3:["HDD"]}))
    
    def test_03_increase_capacity_2 (self):
        self.Controller_Instance_Laptop.set_capacity(2)
        self.Controller_Instance_Laptop.fill_unused_instance_space(self.Controller_Instance_Laptop)

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD],
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], []], 
                                                         backup_storage_directories=[[8, 9], [1, 2, 3, 4, 5], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone"], 1:["USB"], 2:["Desktop"], 3:["HDD"]}))

    def test_04_reduce_capacity_1 (self):
        self.Standard_Instance_Desktop.set_capacity(3)

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD], 
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], []], 
                                                         backup_storage_directories=[[8, 9], [1, 2, 3, 4, 5], [1, 2, 3, 6, 7], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone"], 1:["USB"], 2:["Desktop"], 3:["HDD"]}))
    
    def test_05_reduce_capacity_2 (self):
        self.Standard_Instance_Phone.set_capacity(2)

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD], 
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], []], 
                                                         backup_storage_directories=[[8, 9], [1, 2, 3, 4, 5], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone"], 1:["USB"], 2:["Desktop"], 3:["HDD"]}))
    

    def test_06_add_system_data (self):
        self.Standard_Instance_HDD.add_to_save([11, 12, 13, 14, 15])
        self.Controller_Instance_Laptop.fill_unused_network_space()

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD], 
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 
                                                         backup_storage_directories=[[8, 9], [1, 2, 3, 4, 5], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone"], 1:["USB"], 2:["Desktop"], 3:["HDD"]}))
    
    def test_07_increase_capacity_3 (self):
        self.Controller_Instance_Laptop.set_capacity(100)
        self.Standard_Instance_USB.set_capacity(100)
        self.Standard_Instance_Phone.set_capacity(100)
        self.Standard_Instance_Desktop.set_capacity(100)
        self.Standard_Instance_HDD.set_capacity(100)
        self.Controller_Instance_Laptop.fill_unused_network_space()

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD], 
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 
                                                         backup_storage_directories=[[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 2, 3, 4, 5, 11, 12, 13, 14, 15], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Phone"], 1:["USB"], 2:["Desktop"], 3:["HDD"], 4:["Laptop"]}))

    def test_08_reduce_capacity_3 (self):
        self.Controller_Instance_Laptop.set_capacity(0)
        self.Standard_Instance_USB.set_capacity(3)
        self.Standard_Instance_Phone.set_capacity(5)
        self.Standard_Instance_Desktop.set_capacity(8)
        self.Standard_Instance_HDD.set_capacity(10)
        self.Controller_Instance_Laptop.set_base_copy()

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD], 
                                                         save_directories=[[1, 2, 3], [], [4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 
                                                         backup_storage_directories=[[], [1, 2, 3], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone", "Desktop"], 1:["USB"], 3:["HDD"]}))
        
    def test_09_remove_system_data (self):
        self.Controller_Instance_Laptop.remove_from_save([1, 3])
        self.Standard_Instance_Phone.remove_from_save(5)
        self.Standard_Instance_Desktop.remove_from_save([7, 9])
        self.Standard_Instance_HDD.remove_from_save([11, 13, 15])

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD], 
                                                         save_directories=[[2], [], [4], [6, 8, 10], [12, 14]], 
                                                         backup_storage_directories=[[], [1, 2, 3], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], 
                                                         copies={0:["Laptop", "Phone", "Desktop", "HDD"], 1:["USB"], 3:["HDD"]}))
    
    def test_10_add_instance (self):
        self.Standard_Instance_Tablet.controller = self.Controller_Instance_Laptop
        self.Standard_Instance_Tablet.add_to_save([16, 17, 18, 19, 20])
        self.Controller_Instance_Laptop.add_instance(self.Standard_Instance_Tablet)

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD, self.Standard_Instance_Tablet], 
                                                         save_directories=[[2], [], [4], [6, 8, 10], [12, 14], [16, 17, 18, 19, 20]], 
                                                         backup_storage_directories=[[], [1, 2, 3], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], []], 
                                                         copies={0:["Laptop", "Phone", "Desktop", "HDD", "Tablet"], 1:["USB"]}))
    
    def test_11_initial_2 (self):
        self.Controller_Instance_Laptop.fill_unused_network_space()

        self.assertTrue(Controller.confirm_network_state([self.Controller_Instance_Laptop, self.Standard_Instance_USB, self.Standard_Instance_Phone, self.Standard_Instance_Desktop, self.Standard_Instance_HDD, self.Standard_Instance_Tablet], 
                                                         save_directories=[[2], [], [4], [6, 8, 10], [12, 14], [16, 17, 18, 19, 20]], 
                                                         backup_storage_directories=[[], [1, 2, 3], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5, 11, 12, 13], [2, 4, 6, 8, 10, 16, 17, 18, 19, 20], [14, 8, 10, 12, 4]], 
                                                         copies={0:["Laptop", "Phone", "Desktop", "Tablet"], 1:["USB"], 2:["HDD"]}))
        self.Controller_Instance_Laptop.print_network()

if __name__ == '__main__':
    unittest.main()