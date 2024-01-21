# ================ PROGRAM UTAMA =================
while True:
    try:
        # Print menu utama
        print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")
        file1 = input("Masukkan nama file input daftar makanan: ")
        file2 = input("Masukkan nama file output: ")

        # Membuka file input dan output
        file_in = open(file1, "r")
        file_out = open(file2, "w")

        # ========= PENGAMBILAN DAFTAR MAKANAN KE 1 =========

        # Mengambil daftar makanan 1 sebagai raw text (belum diolah)
        raw_string1 = ""
        for line in file_in:
            if f'Daftar Makanan 1:' in line:
                # Potong teks sehingga hanya teks makanan yang tersisa
                start_index = line.index(":") + 1
                raw_string1 = line[start_index:].strip()
                break
        raw_string1 = raw_string1.lower()

        # Menghapus makanan yang sama
        string1 = "" # String kosong untuk nanti diisi
        i = 0
        while i < len(raw_string1):
            # Define indeks untuk proses setiap item makanan dalam teks raw
            j = i
            # Mencari makanan saat ini sampai koma berikutnya atau akhir string
            while j < len(raw_string1) and raw_string1[j] != ',':
                j += 1
            food_item = raw_string1[i:j]
            # Menambahkan makanan ke string kosong jika belum ada
            if food_item not in string1:
                if string1 != "":
                    string1 += ","
                string1 += food_item
            # Pindah ke makanan berikutnya
            i = j + 1

        # ========= PENGAMBILAN DAFTAR MAKANAN KE 2 =========

        # Mengambil daftar makanan 1 sebagai raw text (belum diolah)
        raw_string2 = ""
        for line in file_in:
            if f'Daftar Makanan 2:' in line:
                # Potong teks sehingga hanya teks makanan yang tersisa
                start_index = line.index(":") + 1
                raw_string2 = line[start_index:].strip()
                break
        raw_string2 = raw_string2.lower()

        # Menghapus makanan yang sama
        string2 = ""
        i = 0
        while i < len(raw_string2):
            # Define indeks untuk proses setiap item makanan dalam teks raw
            j = i
            # Mencari makanan saat ini sampai koma berikutnya atau akhir string
            while j < len(raw_string2) and raw_string2[j] != ',':
                j += 1
            food_item = raw_string2[i:j]
            # Menambahkan makanan ke string kosong jika belum ada
            if food_item not in string2:
                if string2 != "":
                    string2 += ","
                string2 += food_item
            # Pindah ke makanan berikutnya
            i = j + 1

        # ================ PROGRAM LANJUTAN =================

        # Print menu file
        while True:
            print("\nApa yang ingin kamu lakukan?"
                + "\n================================================"
                + "\n1. Tampilkan daftar makanan pertama"
                + "\n2. Tampilkan daftar makanan kedua"
                + "\n3. Tampilkan gabungan makanan dari dua daftar"
                + "\n4. Tampilkan makanan yang sama dari dua daftar"
                + "\n5. Keluar"
                + "\n================================================")
            menu = input("Masukkan aksi yang ingin dilakukan: ")
            print("")

            # Jika pilihan adalah 1
            if menu == "1":
                out_input = "Daftar makanan pertama:\n" + string1
                print(out_input)
                file_out.write(out_input + "\n\n") # Menulis hasil ke file output

            # Jika pilihan adalah 2
            elif menu == "2":
                out_input = "Daftar makanan kedua:\n" + string2
                print(out_input)
                file_out.write(out_input + "\n\n") # Menulis hasil ke file output

            # Jika pilihan adalah 3
            elif menu == "3":
                combined_string = string1 + "," + string2 # Menyatukan kedua string
                result_string = ""
                while combined_string:
                    # Memproses makanan hingga koma berikutnya dalam gabungan string
                    food, sep, combined_string = combined_string.partition(",")
                    # Kalau tidak sama, ditambahkan ke string kosong
                    if food not in result_string:
                        result_string += food + ","
                # Menghapus koma di akhir string
                result_string = result_string[:-1]

                out_input = ("Gabungan makanan favorit dari kedua daftar:\n" + result_string)
                print(out_input)
                file_out.write(out_input + "\n\n") # Menulis hasil ke file output

            # Jika pilihan adalah 4
            elif menu == "4":
                common_foods = "" # String kosong untuk makanan yang sama
                food = "" # String kosong untuk menampung makanan

                for char in string1:
                    if char != ",":
                        food += char  # Menambahkan karakter ke item makanan saat ini
                    else:
                        if food in string2 and (food + ",") not in common_foods:
                            # Memeriksa apakah item makanan saat ini ada di daftar ke-2
                            # dan belum ada dalam string common_foods (makanan yang sama)
                            common_foods += food + ","  # Menambahkan item makanan yang sama
                        food = ""  # Mereset item makanan saat ini untuk item berikutnya dalam string1

                # Memeriksa item makanan terakhir di string1
                if food in string2 and (food + ",") not in common_foods:
                    common_foods += food + ","

                # Menghapus koma di akhir string common_foods jika ada
                if common_foods.endswith(","):
                    common_foods = common_foods[:-1]

                if common_foods == "":
                    # Jika tidak ada yang sama
                    out_input = ("Tidak ada makanan yang sama dari kedua daftar.")
                else:
                    out_input = ("Makanan yang sama dari dua daftar:\n" + common_foods)
                
                print(out_input)
                file_out.write(out_input + "\n\n") # Menulis hasil ke file output

            elif menu == "5":
                # Menutup kedua file
                file_in.close() 
                file_out.close()
                print(f"Terima kasih telah menggunakan program ini!\nSemua keluaran telah disimpan pada file {file2}")
                exit()

            # Validasi input menu
            else:
                print("Input invalid!")
                continue

    # Menangkap error FileNotFoundError saat file tidak ada
    except FileNotFoundError:
        print("Maaf, file input tidak ada")
        continue

    # Menangkap error value, bukan menangkap semua error karena mempermudah CTRL + C saat ingin terminate program
    except ValueError:
        print("Input invalid!")
        continue

