# Menampilkan selamat datang
print("SELAMAT DATANG MAHASISWA BARU UI!\nSilakan input data-data berikut untuk dibuatkan teks perkenalan dirinya :D\n\n" + "="*40 + "\n")

# Meminta user untuk input nama lengkap, nama panggilan, fakultas, jurusan, dan motivasi memilih jurusan tersebut
nama_lengkap = input("Nama lengkap kamu siapa?\nJawab: ")
nama_panggilan = input("Biasa dipanggil siapa?\nJawab: ")
fakultas = input("Kamu dari fakultas apa (tanpa 'Fakultas')?\nJawab: ")
jurusan = input("Kalo jurusannya (tanpa 'Jurusan')?\nJawab: ")
jalur_masuk = input("Kamu masuk lewat jalur apa?\nJawab: ")
motivasi = input("Emangnya apa sih motivasi kamu milih jurusan ini?\nJawab: ")
motto = input("Coba tuliskan motto yang kamu pegang sekarang!\nJawab:")

# Menampilkan hasil input (output) dengan menggunakan f-string agar lebih efisien
print("\n" + "="*40 + f'\n\nHalooo! Namaku adalah {nama_lengkap}, kamu bisa panggil aku {nama_panggilan}. Aku dari Fakultas  {fakultas}, Jurusan {jurusan}. Aku diterima di UI lewat jalur {jalur_masuk}. Aku punya motivasi yang besar untuk aku diterima di UI, yaitu {motivasi}. Motto-ku adalah "{motto}". ')