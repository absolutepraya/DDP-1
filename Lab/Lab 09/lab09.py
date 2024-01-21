class Person:
    # Constructor
    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    # Name getter
    def get_name(self):
        return self.__name

    # Payment getter
    def get_payment(self):
        return self.__payment

    # Stamina getter
    def get_stamina(self):
        return self.__stamina

    # Total work getter
    def set_stamina(self, stamina):
        self.__stamina = stamina

    # Total work getter
    def get_total_work(self):
        return self.__total_work

    # Total work setter
    def set_total_work(self, total_work):
        self.__total_work = total_work

    # Method to calculate the payment
    def pay_day(self):
        return self.__payment * self.__total_work

    # Method to check if the person is available to work
    def is_available(self, cost_stamina):
        return self.__stamina >= cost_stamina

    # Method to work
    def work(self, cost_stamina):
        self.__stamina -= cost_stamina
        self.__total_work += 1

    # Method to print the object
    def __str__(self):
        # Get all the attributes
        class_name = self.__class__.__name__
        name = self.__name
        total_work = self.__total_work
        stamina = self.__stamina
        payday = self.pay_day()
        # Return the string
        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payday:20}"


class Worker(Person):
    # Constructor
    def __init__(self, name):
        super().__init__(name, payment=5000, stamina=100)
        self.__bonus = 0

    # Bonus getter
    def get_bonus(self):
        return self.__bonus

    # Bonus setter
    def set_bonus(self, bonus):
        self.__bonus = bonus

    # Method to work
    def work(self, bonus, cost_stamina):
        # Check if the worker is available
        if self.is_available(cost_stamina):
            # Reduce the worker's stamina by cost_stamina
            self.set_stamina(self.get_stamina() - cost_stamina)
            # Increase the worker's total work by 1
            self.set_total_work(self.get_total_work() + 1)
            # Increase the worker's bonus by bonus
            self.set_bonus(self.get_bonus() + bonus)
        else:
            print("Stamina tidak cukup")
    
    # Method to print the object
    def __str__(self):
        # Get all the attributes
        class_name = self.__class__.__name__
        name = self.get_name()
        total_work = self.get_total_work()
        stamina = self.get_stamina()
        # Worker's payment is the sum of the payday and the bonus
        payday = self.pay_day() + self.get_bonus()
        # Return the string
        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payday:20}"


class Manager(Person):
    # Constructor
    def __init__(self, name, payment, stamina, list_worker:list = []):
        super().__init__(name, payment, stamina)
        self.__list_worker = list_worker
    
    # Getter for list_worker
    def get_list_worker(self):
        return self.__list_worker

    # Method to add a new worker to the list
    def hire_worker(self, name):
        # Check if the worker's name is already in the list
        for worker in self.__list_worker:
            if worker.get_name() == name.title():
                print("Sudah ada!")
                # Decrease the manager's stamina by 10
                self.set_stamina(self.get_stamina() - 10)
                return
            
        print("Berhasil mendapat pegawai baru")
        self.__list_worker.append(Worker(name.title()))
        # Give the manager a work
        self.work(10)
    
    # Method to remove a worker from the list
    def fire_worker(self, name):
        # Check if the worker's name is in the list
        for worker in self.__list_worker:
            if worker.get_name() == name.title():
                print(f"Berhasil memecat {name}")
                # Remove the worker from the list
                self.__list_worker.remove(worker)
                # Give the manager a work
                self.work(10)
                return
            
        print("Nama tidak ditemukan")
        # Decrease the manager's stamina by 10
        self.set_stamina(self.get_stamina() - 10)

    # Method to give a work to a worker, add bonus to the worker, and reduce the worker stamina
    def give_work(self, name, bonus, cost_stamina):
        # Base boolean for the worker's availability
        available = True
        # Check if the worker's name is in the list
        for worker in self.__list_worker:
            if worker.get_name() == name.title():
                # Check if the worker is available
                if worker.is_available(cost_stamina):
                    print("Pegawai dapat menerima pekerjaan\n" +
                            "========================================\n" +
                            f"Berhasil memberi pekerjaan kepada {name}\n")
                    # Give the work to the worker
                    worker.work(bonus, cost_stamina)
                    # Add the manager's total work by 1
                    self.set_total_work(self.get_total_work() + 1)
                else:
                    print("Pegawai tidak dapat menerima pekerjaan. Stamina pegaiwai tidak cukup.")
                break
            else:
                available = False
        if not available:
            print("Nama tidak ditemukan")
        # Decrease the manager's stamina by 10
        self.set_stamina(self.get_stamina() - 10)


# ——————————————————— MAIN PROGRAM ———————————————————


def main():
    # User input
    name =  input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    # Create the manager object
    manager = Manager(name, payment, stamina)

    # While the manager is available, show the menu
    while manager.is_available(1):
        print("\nPACILOKA\n" +
                "-----------------------\n" +
                "1. Lihat status pegawai\n" +
                "2. Beri tugas\n" +
                "3. Cari pegawai baru\n" +
                "4. Pecat pegawai\n" +
                "5. Keluar\n" +
                "-----------------------\n")
        
        # User input for menu
        menu = input("Masukkan pilihan: ")
        
        # If the user input is 1, show the status of the workers
        if menu == "1":
            # Print the manager's status
            print(manager)
            # Print the workers' status
            for worker in manager.get_list_worker():
                print(worker)

        # If the user input is 2, give a work to a worker
        elif menu == "2":
            # User input for the worker's name
            worker_name = input("Tugas akan diberikan kepada: ")
            # User input for the bonus
            bonus = int(input("Bonus pekerjaan: "))
            # User input for the cost stamina
            cost_stamina = int(input("Beban stamina: "))
            # Give the work to the worker
            manager.give_work(worker_name, bonus, cost_stamina)

        # If the user input is 3, hire a new worker
        elif menu == "3":
            # User input for the worker's name
            worker_name = input("Masukkan nama pegawai: ")
            # Hire the worker
            manager.hire_worker(worker_name)

        # If the user input is 4, fire a worker
        elif menu == "4":
            # User input for the worker's name
            worker_name = input("Nama pegawai yang akan dipecat: ")
            # Fire the worker
            manager.fire_worker(worker_name)

        # If the user input is 5, stop the program
        elif menu == "5":
            print("\n----------------------------------------\n" +
                    "Berhenti mengawasi hotel, sampai jumpa !\n" +
                    "----------------------------------------")
            return
        
        # Menu input is not available
        else:
            print("Pilihan tidak tersedia")

    # If the manager's stamina is depleted, print the message
    print("\n----------------------------------------\n" +
            "Stamina manajer sudah habis, sampai jumpa !\n" +
            "----------------------------------------")

# Call the main program
if __name__ == "__main__":
    main()