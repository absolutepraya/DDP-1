"""
    Nama: Ramy, Suta, Abhip
"""

# Create a class called Company
class Company:
    # Create a constructor
    def __init__(self, name:str, drivers:list):
        self.name = name
        self.drivers = drivers

# Create a class called User
class User:
    # Create a constructor
    def __init__(self, name:str):
        self.name = name
    
    def pesan_antar_jemput(self, company:Company):
        eligible_driver = None
        for driver in company.drivers:
            if not driver.is_working:
                eligible_driver = driver
                break
        
        if eligible_driver is None:
            print("No driver please try again")
        else:
            print("Order processed")
            eligible_driver.ride(self)

    def pesan_makanan(self, company:Company):
        eligible_driver = None
        for driver in company.drivers:
            if not driver.is_working:
                eligible_driver = driver
                break
        
        if eligible_driver is None:
            print("No driver please try again")
        else:
            print("Order processed")
            eligible_driver.delivery_food(self)
    
    def pesan_belanja(self, company:Company):
        eligible_driver = None
        for driver in company.drivers:
            if not driver.is_working:
                eligible_driver = driver
                break
        
        if eligible_driver is None:
            print("No driver please try again")
        else:
            print("Order processed")
            eligible_driver.shopping(self)

# Create Driver class
class Driver:
    # Create constructor
    def __init__(self, name:str, is_working:bool=False):
        self.name = name
        self.is_working = is_working
    
    # Create method to start working
    def ride(self, user:User):
        self.is_working = True
        print(f"{self.name} mengantar {user.name}")
    
    # Create method to stop working
    def complete_task(self):
        self.is_working = False

class FoodDelivery(Driver):
    # Create constructor
    def __init__(self, name:str, is_working:bool=False):
        super().__init__(name, is_working)

    def delivery_food(self, user:User):
        print(f"{self.name} memesan makanan {user.name}")
        # Change the is_working attribute to True
        self.is_working = True

class MartAssistance(Driver):
    # Create constructor
    def __init__(self, name:str, is_working:bool=False):
        super().__init__(name, is_working)

    def shopping(self, user:User):
        print(f"{self.name} belanja pesanan {user.name}")
        # Change the is_working attribute to True
        self.is_working = True

# Test case
driver_aja = Driver("otong")
food_driver = FoodDelivery("anjas")
mart_assistance = MartAssistance("bintang")
list_of_drivers = [driver_aja, food_driver, mart_assistance]
company = Company("Jekgo", list_of_drivers)
user_a = User("a")
user_b = User("b")
user_c = User("c")
user_d = User("d")

user_a.pesan_antar_jemput(company)
user_b.pesan_makanan(company)
user_c.pesan_belanja(company)
user_d.pesan_antar_jemput(company)