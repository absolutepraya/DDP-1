# Meminta user untuk menginput pesan hex code yang diterima dari bangsa Zog
hex_zog = input("Pesan Kelompok Zog: ")

# Meminta user untuk menginput 2-digits clue yang diterima dari bangsa Zog
angka1 = int(input("Angka 1: "))
angka2 = int(input("Angka 2: "))

# Translasi pesan hex code menjadi bahasa manusia dalam bentuk string ASCII
bytes_zog = bytes.fromhex(hex_zog)
ascii_zog = bytes_zog.decode("ASCII")

# Mengubah 2-digits clue menjadi password dalam bentuk binary
password_zog = bin(angka1 * angka2 * 13)

# Output hasil terjemahan & password dengan f-string
print(f"\nHasil terjemahan pesan: {ascii_zog}" +
    f"\nPassword: {password_zog}" +
    f'\n\nPesan "{ascii_zog}" telah diterima dengan password "{password_zog}".')