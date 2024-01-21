list_nama = [] # List kosong untuk database nama
list_nilai = [] # List kosong untuk database nilai

while True:
    # Menampilkan menu utama
    print("Selamat datang di Database Nilai Dek Depe" +
        "\n1. Tambah data ke database" +
        "\n2. Baca data dari database" +
        "\n3. Update data di database" +
        "\n4. Hapus data di database" +
        "\n5. Keluar")
    # Input menu
    menu = input("Masukkan kegiatan yang ingin dilakukan: ")

    # JIKA PILIHAN MENU ADALAH 1 ================================
    if menu == "1":
        nama = input("Masukkan nama: ")
        # Jika nama sudah ada di dalam database, maka akan kembali ke menu utama
        if nama.lower() in list_nama:
            print("Nama sudah terdapat di dalam database\n")
            continue
        else: # Memasukkan nama ke database
            list_nama.append(nama.lower())

        nilai = 0 # Variabel nilai untuk looping
        counter = 0 # Variabel counter untuk mengetahui banyak nilai yang dimasukkan
        temp_list = [] # List sementara untuk menampung nilai
        
        while nilai != "STOP":
            while True:
                # Input nilai
                nilai = input(f"Masukkan nilai Lab {counter + 1} (ketik STOP untuk selesai): ")
                try:
                    # Jika input nilai adalah STOP, maka akan berhenti
                    if nilai.upper() == "STOP": 
                        nilai = "STOP"
                        break
                    # Kembali menampilkan input nilai jika nilai tidak valid
                    elif float(nilai) > 100 or float(nilai) < 0:
                        print("Nilai tidak valid!")
                        continue
                except ValueError: # Menangkap error jika input nilai bukan angka
                    print("Nilai tidak valid!")
                    continue
                
                # Memasukkan nilai ke list sementara
                temp_list.append(float(nilai))
                
                counter += 1 # Menambah counter banyak nilai
                break
        
        # Memasukkan list sementara ke list nilai
        list_nilai.append(temp_list)
        print(f"Berhasil menambahkan {counter} nilai untuk {nama} ke database\n")
    
    # JIKA PILIHAN MENU ADALAH 2 ================================
    elif menu == "2":
        # Jika nama tidak di database, maka akan kembali ke menu utama
        nama = input("Masukkan nama: ")
        if nama.lower() not in list_nama:
            print("Nama tidak ada dalam database\n")
            continue
        # Masuk ke list nilai nama tersebut
        index_nilai = list_nama.index(nama.lower())       
        try:
            # Input lab ke-n
            lab_n = int(input("Masukkan nilai Lab ke berapa yang ingin dilihat: "))
            # Jika lab ke-n tidak ada di database, maka akan kembali ke menu utama
            if lab_n > len(list_nilai[index_nilai]) or lab_n < 1 or list_nilai[index_nilai][lab_n - 1] == None:
                print(f"Tidak terdapat nilai untuk Lab {lab_n}\n")
                continue
        except ValueError: # Menangkap error jika input lab bukan angka
            print("Input tidak valid\n")
            continue

        # Menampilkan nilai lab ke-n
        print(f"Nilai Lab {lab_n} {nama} adalah {list_nilai[index_nilai][lab_n - 1]:.1f}\n")
    
    # JIKA PILIHAN MENU ADALAH 3 ================================
    elif menu == "3":
        # Jika nama tidak di database, maka akan kembali ke menu utama
        nama = input("Masukkan nama: ")
        if nama.lower() not in list_nama:
            print("Nama tidak ada dalam database\n")
            continue
        # Masuk ke list nilai nama tersebut
        index_nilai = list_nama.index(nama.lower())
        try:
            # Input lab ke-n
            lab_n = int(input("Masukkan nilai Lab ke berapa yang ingin diupdate: "))
            # Jika lab ke-n tidak ada di database, maka akan kembali ke menu utama
            if lab_n > len(list_nilai[index_nilai]) or lab_n < 1 or list_nilai[index_nilai][lab_n - 1] == None:
                print(f"Tidak terdapat nilai untuk Lab {lab_n}\n")
                continue
        except ValueError: # Menangkap error jika input lab bukan angka
            print("Input tidak valid\n")
            continue
        
        while True:
            try:
                # Input nilai baru
                nilai_update = float(input("Masukkan nilai baru: "))
                # Jika nilai baru tidak valid, maka akan kembali ke input nilai baru
                if nilai_update > 100 or nilai_update < 0:
                    print("Nilai tidak valid!")
                    continue
                # Berhasil mengupdate nilai
                else:
                    print(f"Berhasil mengupdate nilai Lab {lab_n} {nama} dari {list_nilai[index_nilai][lab_n - 1]:.1f} ke {nilai_update:.1f}\n")
                    # Mengupate nilai
                    list_nilai[index_nilai][lab_n - 1] = nilai_update
                    break
            except ValueError: # Menangkap error jika input nilai bukan angka
                print("Input tidak valid\n")
                continue

    # JIKA PILIHAN MENU ADALAH 4 ================================
    elif menu == "4":
        # Jika nama tidak di database, maka akan kembali ke menu utama
        nama = input("Masukkan nama: ")
        if nama.lower() not in list_nama:
            print("Nama tidak ada dalam database\n")
            continue
        # Masuk ke list nilai nama tersebut
        index_nilai = list_nama.index(nama.lower())
        try:
            # Input lab ke-n
            lab_n = int(input("Masukkan nilai Lab ke berapa yang ingin dihapus: "))
            # Jika lab ke-n tidak ada di database, maka akan kembali ke menu utama
            if lab_n > len(list_nilai[index_nilai]) or lab_n < 1 or list_nilai[index_nilai][lab_n - 1] == None:
                print(f"Tidak terdapat nilai untuk Lab {lab_n}\n")
                continue
        except ValueError: # Menangkap error jika input lab bukan angka
            print("Input tidak valid\n")
            continue

        # Agar index nilai yang lain tidak berubah, cukup diubah menjadi none
        list_nilai[index_nilai][lab_n - 1] = None

        # Menampilkan pesan berhasil menghapus nilai
        print(f"Berhasil menghapus nilai Lab {lab_n} {nama} dari database\n")
    
    # JIKA PILIHAN MENU ADALAH 5 ================================
    elif menu == "5":
        print("Terimakasih telah menggunakan Database Nilai Dek Depe\n")
        break

    # Validasi input menu
    else:
        print("Menu tidak tersedia\n")