import time

class ParkingLot:
    def __init__(self):
        self.capacity = 10
        self.available_spaces = 10
        self.parked_cars = {}

    def park_car(self, car_number):
        if self.available_spaces == 0:
            print("Maaf, tempat parkir sudah penuh. 😓")
            return False
        else:
            self.parked_cars[car_number] = time.time()
            self.available_spaces -= 1
            print(f"Mobil dengan plat nomor {car_number} berhasil parkir.")
            return True

    def leave_car(self, car_number):
        if car_number not in self.parked_cars:
            print(f"Mobil dengan plat nomor {car_number} tidak diparkirkan di sini.")
            return False
        else:
            start_time = self.parked_cars[car_number]
            end_time = time.time()
            elapsed_time = end_time - start_time
            parking_fee = elapsed_time // 10 * 1000
            del self.parked_cars[car_number]
            self.available_spaces += 1
            print(f"Mobil dengan plat nomor {car_number} meninggalkan tempat parkir.\n" +
                f"Waktu parkir: {int(elapsed_time)} detik\n" +
                f"Biaya parkir: Rp. {parking_fee}")
            return True

# Contoh penggunaan
parkir_boulevard = ParkingLot()

parkir_boulevard.park_car("N 45 GOR")
parkir_boulevard.park_car("S 14 KNG")

# Ceritanya mobil 1 sudah terparkir selama 25 detik
parkir_boulevard.leave_car("N 45 GOR")

# Ceritanya mobil 2 sudah terparkir selama 50 detik
parkir_boulevard.leave_car("S 14 KNG")