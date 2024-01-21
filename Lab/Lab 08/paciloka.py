# Create a class called Hotel to store information about a hotel
class Hotel:

    # Defining the constructor
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest = []

    # Defining the booking method
    def booking(self, guest_name, room_booked):
        self.available_room -= room_booked
        self.profit += self.room_price*room_booked
        # Append the guest name to the guest list if the guest is not in the guest list
        if guest_name not in self.guest:
            self.guest.append(guest_name)
        # Print the success message
        print(f"User dengan nama {guest_name} berhasil melakukan booking di hotel {self.name} dengan jumlah {room_booked} kamar!")

    # Defining the __str__ method to print the hotel information
    def __str__(self):
        return f"Hotel dengan nama {self.name} mempunyai profit sebesar {self.profit}"

# Create a class called User to store information about a user
class User:

    # Defining the constructor
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotels_booked = []

    # Defining the topup method
    def topup(self, amount):
        self.money += amount

    # Defining the __str__ method to print the user information
    def __str__(self):
        return f"User dengan nama {self.name} mempunyai saldo sebesar {self.money}"


# ———————————————————— MAIN PROGRAM ————————————————————


# Input the amount of hotels and users
hotels_amount = int(input("Masukkan banyak hotel : "))
users_amount = int(input("Masukkan banyak user : "))
print()

# Create a list to store the hotel objects and user objects
hotel_list = []
user_list = []

# Hotel input looping
for hotel in range(hotels_amount):
    hotel_name = input(f"Masukkan nama hotel ke-{hotel+1} : ")
    hotel_available_room = int(input(f"Masukkan banyak kamar hotel ke-{hotel+1} : "))
    hotel_room_price = int(input(f"Masukkan harga satu kamar hotel ke-{hotel+1} : "))
    # Create the hotel object
    hotel = Hotel(hotel_name, hotel_available_room, hotel_room_price)
    # Append the hotel object to the hotel_list
    hotel_list.append(hotel)

print()

# User input looping
for user in range(users_amount):
    user_name = input(f"Masukkan nama user ke-{user+1} : ")
    user_money = int(input(f"Masukkan saldo user ke-{user+1} : "))
    # Create the user object
    user = User(user_name, user_money)
    # Append the user object to the user_list
    user_list.append(user)

# Menu looping
while True:
    print("\n=============Welcome to Paciloka!=============\n")

    # Print the hotel information
    menu = input("Masukkan perintah : ")

    # If menu is 1, print the listed hotels and users
    if menu == "1":

        # Print the hotel list
        print("Daftar Hotel")
        for hotel in range(len(hotel_list)):
            print(f"{hotel+1}. {hotel_list[hotel].name}")

        # Print the user list
        print("\nDaftar User")
        for user in range(len(user_list)):
            print(f"{user+1}. {user_list[user].name}")
    
    # If menu is 2, print the hotel information
    elif menu == "2":

        hotel_name = input("Masukkan nama hotel : ")
        # Check if the hotel is not in the hotel_list
        if hotel_name not in [hotel.name for hotel in hotel_list]:
            print("Nama hotel tidak ditemukan di sistem!")
            continue

        # Find the hotel object in the hotel_list
        for hotel in range(len(hotel_list)):
            if hotel_list[hotel].name == hotel_name:
                # Print the hotel information using __str__ method
                print(hotel_list[hotel].__str__())
    
    # If menu is 3, print the user information
    elif menu == "3":

        user_name = input("Masukkan nama user : ")
        # Check if the user is not in the user_list
        if user_name not in [user.name for user in user_list]:
            print("Nama user tidak ditemukan di sistem!")
            continue

        # Find the user object in the user_list
        for user in range(len(user_list)):
            if user_list[user].name == user_name:
                # Print the user information using __str__ method
                print(user_list[user].__str__())
    
    # If menu is 4, add money to the user's balance
    elif menu == "4":

        user_name = input("Masukkan nama user : ")
        # Check if the user is not in the user_list
        if user_name not in [user.name for user in user_list]:
            print("Nama user tidak ditemukan di sistem!")
            continue

        # Find the user object in the user_list
        for user in range(len(user_list)):
            if user_list[user].name == user_name:

                try:
                    amount = int(input("Masukkan jumlah uang yang akan ditambahkan ke user : "))
                    # Check if amount is 0 or less
                    if amount <= 0:
                        print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
                        break
                except ValueError:
                    print("Masukkan jumlah uang yang valid!")
                    break

                # Add the money to the user's balance
                user_list[user].topup(amount)

                # Print the success message
                print(f"Berhasil menambahkan {amount} ke user {user_list[user].name}. Saldo user menjadi {user_list[user].money}")
                break
    
    # If menu is 5, book a room
    elif menu == "5":

        user_name = input("Masukkan nama user : ")
        # Check if the user is not in the user_list
        if user_name not in [user.name for user in user_list]:
            print("Nama user tidak ditemukan di sistem!")
            continue

        hotel_name = input("Masukkan nama hotel : ")
        # Check if the hotel is not in the hotel_list
        if hotel_name not in [hotel.name for hotel in hotel_list]:
            print("Nama hotel tidak ditemukan di sistem!")
            continue

        try:
            room_booked = int(input("Masukkan jumlah kamar yang akan di-booking : "))
            # Check if room_booked is not an integer
            if not isinstance(room_booked, int):
                print("Masukkan jumlah kamar yang valid!")
                continue
            # Check if the room_booked is 0 or less
            if room_booked <= 0:
                print("Jumlah kamar yang akan dibooking harus lebih dari 0!")
                continue
        except ValueError:
            # If room_booked is not an integer, print the message
            print("Masukkan jumlah kamar yang valid!")
            continue

        # Find the user object in the user_list
        for user in range(len(user_list)):
            if user_list[user].name == user_name:

                # Find the hotel object in the hotel_list
                for hotel in range(len(hotel_list)):
                    if hotel_list[hotel].name == hotel_name:

                        # Check if the room_booked is more than the available room
                        if room_booked > hotel_list[hotel].available_room:
                            print("Booking tidak berhasil!")
                            continue

                        # If user has enough money, book the room
                        if user_list[user].money >= hotel_list[hotel].room_price*room_booked:
                            # Reduce the user's balance
                            user_list[user].money -= hotel_list[hotel].room_price*room_booked
                            # Add the hotel name to the user's booked hotels list (if it's not already in the list)
                            if hotel_list[hotel].name not in user_list[user].hotels_booked:
                                user_list[user].hotels_booked.append(hotel_list[hotel].name)
                            # Book the room
                            hotel_list[hotel].booking(user_list[user].name, room_booked)
                            break

                        # If user does't have enough money, print the message
                        else:
                            print("Saldo user tidak cukup.")
                            break

                break
    
    # If menu is 6, print the hotel's guest list
    elif menu == "6":

        hotel_name = input("Masukkan nama hotel : ")
        # Check if the hotel is not in the hotel_list
        if hotel_name not in [hotel.name for hotel in hotel_list]:
            print("Nama hotel tidak ditemukan di sistem!")
            continue

        # Find the hotel object in the hotel_list
        for hotel in range(len(hotel_list)):
            if hotel_list[hotel].name == hotel_name:

                # If the hotel has no guest, print the message
                if len(hotel_list[hotel].guest) == 0:
                    print(f"Hotel {hotel_list[hotel].name} tidak memiliki pelanggan!")
                    break

                # Print the guest list using looping
                print(f"{hotel_name} | ", end="")
                for guest in range(len(hotel_list[hotel].guest)):
                    # If it's the last guest in the list, print the guest name without comma
                    if guest == len(hotel_list[hotel].guest)-1:
                        print(f"{hotel_list[hotel].guest[guest]}")
                    else:
                        print(f"{hotel_list[hotel].guest[guest]}, ", end="")

                break

    # If menu is 7, print user's booking history
    elif menu == "7":

        user_name = input("Masukkan nama user : ")
        # Check if the user is not in the user_list
        if user_name not in [user.name for user in user_list]:
            print("Nama user tidak ditemukan di sistem!")
            continue

        # Find the user object in the user_list
        for user in range(len(user_list)):
            if user_list[user].name == user_name:

                # If the user has no booking history, print the message
                if len(user_list[user].hotels_booked) == 0:
                    print(f"User {user_list[user].name} tidak pernah melakukan booking!")
                    break

                # Print the booking history using looping
                print(f"{user_name} | ", end="")
                for hotel in range(len(user_list[user].hotels_booked)):
                    # If it's the last hotel in the list, print the hotel name without comma
                    if hotel == len(user_list[user].hotels_booked)-1:
                        print(f"{user_list[user].hotels_booked[hotel]}")
                    else:
                        print(f"{user_list[user].hotels_booked[hotel]}, ", end="")

                break

    # If menu is 8, exit the program
    elif menu == "8":
        print("Terima kasih sudah mengunjungi Paciloka!")
        break

    # Menu input validation
    else:
        print("Perintah tidak diketahui! Masukkan perintah yang valid")