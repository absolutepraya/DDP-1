while True:
    try:
        # Menampilkan menu utama
        print("Selamat Datang di Toko Buku Place Anak Chill"
        + "\n" + "="*44
        + "\n1. Pinjam buku"
        + "\n2. Keluar"
        + "\n" + "="*44)

        # Menerima input pilihan dari pengguna
        menu_pilihan = int(input("Apa yang ingin anda lakukan: "))

        # User memilih pilihan 1 (pinjam buku)
        if menu_pilihan == 1:
            
            # Meminta nama, saldo, dan status membership
            nama = input("Masukkan nama anda: ")
            saldo = int(input("Masukkan saldo anda: "))
            member = input("Apakah anda member? [Y/N]: ").upper() # DIJAMIN VALID
            
            # Jika pengguna adalah member, akan masuk ke loop validasi ID member
            if member == "Y":
                error_count = 0
                # Loop validasi member
                while True:
                    if error_count == 3: # Validasi bernilai false jika gagal input ID 3x
                        print("Anda gagal memasukkan ID yang valid sebanyak 3x. Kembali ke menu utama.\n")
                        validasi_id = False
                        break
                    id = input("Masukkan ID anda: ")
                    # Penjumlahan digit ID menggunakan indexing string
                    id_sum = int(id[0]) + int(id[1]) + int(id[2]) + int(id[3]) + int(id[4])
                    if id_sum != 23:
                        error_count += 1
                        print("ID tidak valid!")
                    elif id_sum == 23: # Validasi bernilai true jika input ID berhasil
                        validasi_id = True
                        break
                if validasi_id == False: # Kembali ke menu utama setelah gagal input ID 3x
                    continue
                elif validasi_id == True: # Masuk ke sistem loop katalog buku setelah berhasil input ID
                    pass
                print("Login member berhasil!")

            # Jika pengguna bukan member, akan langsung masuk ke sistem loop katalog buku
            else:
                print("Login non-member berhasil!")
            
            # Loop katalog buku
            while True:
                # Menampilkan katalog buku
                print("\n" + "="*44
                    + "\nKatalog Buku Place Anak Chill"
                    + "\n" + "="*44
                    + "\nX-Man (Rp 7.000/hari)"
                    + "\nDoraemoh (Rp 5.500/hari)"
                    + "\nNartoh (Rp 4.000/hari)"
                    + "\n" + "="*44
                    + "\nExit"
                    + "\n" + "="*44)
                
                # Menerima input buku yang dipilih
                buku_pilihan = input("Buku yang dipilih: ")
                
                # Jika pengguna memilih keluar, keluar dari loop katalog buku
                if buku_pilihan.lower() == "exit":
                    print("\n" + "="*44)
                    break
                
                # Menerima input lama peminjaman buku
                lama_pinjam = int(input("Ingin melakukan peminjaman untuk berapa hari: "))

                # Memeriksa apakah buku yang dipilih tersedia di katalog
                if buku_pilihan.lower() != "x-man" and buku_pilihan.lower() != "doraemoh" and buku_pilihan.lower() != "nartoh":
                    print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!")
                    continue
                
                """Menghitung harga peminjaman sesuai dengan membership pelanggan,
                jika pelanggan adalah member maka diskon 20% (80% * harga = 0,8 * harga),
                jika pelanggan bukan member maka harga penuh"""
                if member == "Y":
                    if buku_pilihan.lower() == "x-man":
                        harga = 0.8 * 7000 * lama_pinjam
                    elif buku_pilihan.lower() == "doraemoh":
                        harga = 0.8 * 5500 * lama_pinjam
                    elif buku_pilihan.lower() == "nartoh":
                        harga = 0.8 * 4000 * lama_pinjam
                else:
                    if buku_pilihan.lower() == "x-man":
                        harga = 7000 * lama_pinjam
                    elif buku_pilihan.lower() == "doraemoh":
                        harga = 5500 * lama_pinjam
                    elif buku_pilihan.lower() == "nartoh":
                        harga = 4000 * lama_pinjam

                """Memeriksa apakah saldo cukup untuk peminjaman, 
                jika cukup maka saldo dikurangi,
                jika tidak cukup program akan kembali menampilkan katalog buku"""
                if saldo < harga:
                    print(f"Tidak berhasil meminjam buku {buku_pilihan}! Saldo anda kurang {harga - saldo}")
                    continue
                else:
                    saldo -= harga

                # Menampilkan informasi peminjaman
                print(f"Berhasil meminjam buku {buku_pilihan} selama {lama_pinjam} hari"
                    + f"\nSaldo anda saat ini {saldo}")

        # User memilih pilihan 2 (keluar)
        elif menu_pilihan == 2:
            print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
            break

    except:
        # Menangani error input yang invalid saat pemilihan menu di menu utama, dan juga yang lain (jika ada)
        print("Perintah tidak diketahui!\n")