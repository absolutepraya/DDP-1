# Membuka file Lab6.txt dan memasukkan isi file ke dalam list contents
with open("Lab6.txt", "r") as file:
    contents = file.readlines()
    
    # Merapihkan isi list contents
    while "\n" in contents:
        contents.remove('\n')
    while "==============================\n" in contents:
        contents.remove("==============================\n")

# Assign dictionary database kosong
database = {}

# Memasukkan isi list contents ke dalam dictionary database
for i in range(0, len(contents), 2):

    # Merapihkan isi credential dan submission dengan strip(), replace(), lalu split()
    credential = contents[i].strip().replace('\n', '').split(";")
    submission = contents[i+1].strip().replace('\n', '')

    # Memasukkan credential dan submission ke dalam dictionary database
    database[tuple(credential)] = submission

# Membuat list tugas yang ada di dalam database
daftar_tugas = []
for key in database:
    daftar_tugas.append(key[2])

# Membuat list NPM yang ada di dalam database
daftar_npm = []
for key in database:
    daftar_npm.append(key[1])

# Membuat list nama yang ada di dalam database
daftar_nama = []
for key in database:
    daftar_nama.append(key[0])

# —————————————————— P R O G R A M   U T A M A ——————————————————

print("Selamat datang di program Plagiarism Checker!")

# Looping program utama
while True:
    print("=====================================================================")

    # Input dan validasi input tugas
    tugas = input("Masukkan nama mata kuliah yang ingin diperiksa: ")
    if tugas.upper() == "EXIT":
        print("Terima kasih telah menggunakan program Plagiarism Checker!")
        break
    elif tugas not in daftar_tugas:
        print(f"{tugas} tidak ditemukan.\n")
        continue
    
    # Input dan validasi input nama/NPM mahasiswa pertama
    nama1 = input("Masukkan nama/NPM mahasiswa pertama: ")
    if nama1 not in daftar_nama and nama1 not in daftar_npm:
        print("Informasi mahasiswa tidak ditemukan.\n")
        continue

    # Mencari NPM atau nama mahasiswa pertama dari informasi yang diinput
    if nama1.isdigit(): # Jika input berupa NPM, diassign dahulu ke variabel npm1
        npm1 = nama1
        for key in database:
            if npm1 == key[1]:
                nama1 = key[0]
                break
    else: # Jika input berupa nama, cari NPM dari nama yang diinput
        for key in database:
            if nama1 == key[0]:
                npm1 = key[1]
                break
    
    # Input dan validasi input nama/NPM mahasiswa kedua
    nama2 = input("Masukkan nama/NPM mahasiswa kedua: ")
    if nama2 not in daftar_nama and nama2 not in daftar_npm:
        print("Informasi mahasiswa tidak ditemukan.\n")
        continue

    # Mencari NPM atau nama mahasiswa kedua dari informasi yang diinput
    if nama2.isdigit(): # Jika input berupa NPM, diassign dahulu ke variabel npm2
        npm2 = nama2
        for key in database:
            if npm2 == key[1]:
                nama2 = key[0]
                break
    else: # Jika input berupa nama, cari NPM dari nama yang diinput
        for key in database:
            if nama2 == key[0]:
                npm2 = key[1]
                break

    print("============================= Hasil =================================")

    # Mencari submission mahasiswa pertama dan kedua, dan merubahnya menjadi list
    submission1 = database[(nama1, npm1, tugas)].split(' ')
    submission2 = database[(nama2, npm2, tugas)].split(' ')

    # Menghilangkan elemen yang ganda atau lebih menggunakan set
    submission1 = set(submission1)
    submission2 = set(submission2)

    # Mencari keyword yang sama dari kedua submission menggunakan intersection
    similar_words = submission1.intersection(submission2)

    # Menghitung tingkat similarity dengan rumus: (jumlah keyword yang sama/jumlah keyword unik) * 100%
    similarity = (len(similar_words)/len(submission1)) * 100

    # Menampilkan hasil
    print(f"Tingkat kemiripan tugas {tugas} {nama1} dan {nama2} adalah {similarity:.2f}%.")

    # Menampilkan indikasi plagiarisme
    if similarity > 70:
        print(f"{nama1} dan {nama2} terindikasi plagiarisme.\n" )
    elif 30 < similarity < 71:
        print(f"{nama1} dan {nama2} terindikasi plagiarisme ringan.\n")
    else:
        print(f"{nama1} dan {nama2} tidak terindikasi plagiarisme.\n")