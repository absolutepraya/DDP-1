import sys
import os
import time
import re # (Regular Expression)


# ===================================== FUNCTIONS =====================================


# Define sebuah function untuk mencari informasi dari file XML
def get_info(text):
    """Cara kerja fungsi (ditandai dengan #NOMOR):
    1. Mencari index dari text yang dicari
    2. Menambahkan panjang text yang dicari ke index yang didapat untuk mendapatkan index awal dari informasi
    3. Mencari index dari tanda petik, dimulai dari index awal informasi untuk mendapatkan index akhir dari informasi
    4. Mengambil informasi dari index awal sampai index akhir"""
    info_start = contents_raw.find(f'{text}="') #1
    info_start += len(f'{text}="') #2
    info_end = contents_raw.find('"', info_start) #
    return contents_raw[info_start:info_end] #4

# Define functions untuk memberi warna pada text
def col_out(text):
    return f"\033[1;34m{text}\033[1;0m" # BIRU
def col_warn(text):
    return f"\033[1;31m{text}\033[1;0m" # MERAH
def col_mc(text):
    return f"\033[1;32m{text}\033[1;0m" # HIJAU

# Define sebuah function untuk mencari kata dengan match case
def mc_search(text):
    """Cara kerja fungsi (ditandai dengan #NOMOR):
    1. Membuat sebuah regex dengan text yang dicari
    2. Mencari apakah regex ada di dalam isi file
    3. Mengembalikan nilai True jika ada, False jika tidak ada"""
    compiled = re.compile(r'\b{}\b'.format(text)) #1
    match = re.search(compiled, contents) #2
    return bool(match) #3


# ==================================== VALIDATIONS ====================================


print()

# Error handling jumlah argumen
argerror = len(sys.argv) < 3 or len(sys.argv) > 6
# Error handling argumen section
sectionerror = sys.argv[1] not in ["kepala_putusan", "identitas", "riwayat_penahanan", "riwayat_perkara", "riwayat_tuntutan", "riwayat_dakwaan", "fakta", "fakta_umum", "pertimbangan_hukum", "amar_putusan", "penutup", "all"]
# Khusus untuk prompt dengan 5 argumen (regular) atau 6 argumen (matchcase)
if len(sys.argv) in [5, 6]:
    # Error handling argumen operator
    operatorerror = sys.argv[3] not in ["AND", "OR", "ANDNOT"]
    # Error handling argumen matchcase
    if len(sys.argv) == 6:
        mcerror = sys.argv[5] not in ["matchcase", "mc"]
    else:
        mcerror = False
# Khusus untuk prompt dengan 4 argumen (matchcase)
else:
    # Error handling argumen matchcase
    if len(sys.argv) == 4:
        mcerror = sys.argv[3] not in ["matchcase", "mc"]
    else:
        mcerror = False
    # Mengabaikan operator error karena tidak ada operator
    operatorerror = False

# Memeriksa apakah argumen program valid atau tidak, jika iya maka akan keluar dari program
if argerror or sectionerror or mcerror:
    print(col_warn("Argumen program tidak benar.\n"))
    sys.exit()
elif operatorerror:
    print(col_warn("Mode harus berupa AND, OR atau ANDNOT.\n"))
    sys.exit()


# ==================================== MAIN PROGRAM ====================================


# Menggunakan try-except untuk validasi tambahan
try:
    # Memasukkan argumen program ke dalam variabel
    search_section = sys.argv[1]
    search_words1 = sys.argv[2].lower()
    # Khusus untuk prompt dengan 5 argumen (regular) atau 6 argumen (matchcase)
    if len(sys.argv) in [5, 6]:
        operator = sys.argv[3]
        search_words2 = sys.argv[4].lower()
        if len(sys.argv) == 6:
            feat = sys.argv[5]
except:
    print(col_warn("Argumen program tidak benar.\n"))

"""Membuat full path ke folder dataset. Nama folder bisa diganti sesuai 
kebutuhan, asalkan file search.py memiliki directory se-level atau lebih 
rendah dengan folder yang dimau, misal:
- join(os.getcwd(), 'database')
- join(os.getcwd(), 'indo-law-main/dataset')"""
folder_path = os.path.join(os.getcwd(), 'dataset')

counter = 0 # Counter dokumen yang ditemukan
mc_counter = 0 # Counter dokumen matchcase
docnums = [] # List nama dokumen yang ditemukan

# Memulai perhitungan waktu
time_start = time.time()

# Looping untuk mendapatkan semua file XML di dalam folder dataset
for dirpath, dirnames, filenames in os.walk(folder_path):
    # Looping untuk membuka setiap file XML yang didapat
    for filename in filenames:
        # Membuat full path ke file XML
        file_path = os.path.join(dirpath, filename)
        # Membuka dan mengambil isi file XML ke dalam variabel
        with open(file_path, 'r', encoding='utf-8') as file:
            contents_raw = file.read().replace('\n', ' ')

        # ———————————— PENGAMBILAN ISI FILE ————————————

        # Jika search_section adalah all, maka akan mengambil semua text dari file XML
        if search_section == "all":
            contents = contents_raw

        # Jika search_section bukan all, maka akan mencari section yang sesuai dan mengambil textnya
        else:
            # Mencari start tag dan end tag dari section yang dicari
            start_tag = f'<{search_section}>'
            end_tag = f'</{search_section}>'
            start_index = contents_raw.find(start_tag)
            end_index = contents_raw.find(end_tag)
            # Memasukkan text dari section yang dicari ke variable
            contents = contents_raw[start_index + len(start_tag):end_index]

        # ——————————————— PENCARIAN FILE ———————————————

        # Mencari keyword pertama dengan match case
        match1 = mc_search(search_words1)

        # Khusus untuk prompt dengan 5 argumen (regular) atau 6 argumen (matchcase)
        if len(sys.argv) in [5, 6]:
            # Mencari keyword kedua dengan match case
            match2 = mc_search(search_words2)

            if operator == "AND": # Kedua keywords harus ada
                if search_words1 in contents and search_words2 in contents:
                    available = True
                    if match1 and match2:
                        highlight = True
                    else:
                        highlight = False
                else:
                    available = False
            elif operator == "OR": # Salah satu keyword harus ada
                if search_words1 in contents or search_words2 in contents:
                    available = True
                    if match1 or match2:
                        highlight = True
                    else:
                        highlight = False
                else:
                    available = False
            elif operator == "ANDNOT": # Keyword pertama harus ada, tapi keyword kedua tidak boleh ada
                if search_words1 in contents and search_words2 not in contents:
                    available = True
                    if match1 and not match2:
                        highlight = True
                    else:
                        highlight = False
                else:
                    available = False
    
        # Khusus untuk prompt dengan 3 argumen (regular) atau 4 argumen (matchcase)
        elif len(sys.argv) in [3, 4]:
            if search_words1 in contents:
                available = True
                if match1:
                    highlight = True
                else:
                    highlight = False
            else:
                available = False
        
        # —————————————— PENCETAKAN HASIL ——————————————

        # Jika keyword terdapat di dalam isi file, maka akan masuk ke kondisi ini
        if available == True:
            # Mendapatkan informasi dari header file XML
            provinsi = get_info("provinsi")[:15]
            klasifikasi = get_info("klasifikasi")[:15]
            sub_klasifikasi = get_info("sub_klasifikasi")[:30]
            lembaga_peradilan = get_info("lembaga_peradilan")[:20]
            # Print hasil informasi yang didapat
            if len(sys.argv) in [3, 5] and highlight == True:
                print(col_mc(f"{filename} {provinsi:>15} {klasifikasi:>15} {sub_klasifikasi:>30} {lembaga_peradilan:>20}"))
                mc_counter += 1
            else:
                print(f"{filename} {provinsi:>15} {klasifikasi:>15} {sub_klasifikasi:>30} {lembaga_peradilan:>20}")
            # Banyak file yang ditemukan bertambah 1
            counter += 1
            # Menambahkan nama file ke dalam list docnums untuk diakses nanti
            docnums.append(filename)

# ——————— PENCETAKAN STATISTIK PENCARIAN ———————

# Menghentikan dan menghitung perhitungan waktu
time_end = time.time()
time_total = time_end - time_start

# Conditionals untuk menampilkan banyak file yang ditemukan dan total waktu pencarian
if counter == 0:
    print("Tidak ada dokumen yang ditemukan.")
else:
    print(f"\n{'Banyaknya dokumen yang ditemukan':<33}= {counter}")
    if len(sys.argv) in [3, 5]:
        print(col_mc(f"{'Jumlah matchcase':<33}= {mc_counter}"))
print(f"{'Total waktu pencarian':<33}= {time_total:.3f} detik")

# Keluar program jika tidak ada dokumen yang ditemukan
if counter == 0:
    sys.exit()

# ——————————————— DETAIL DOKUMEN ———————————————

print("\n" + "—"*125 + "\n")

# Looping validasi input
while True:
    moreinfo = input("Apakah Anda mau melihat informasi lebih lanjut mengenai dokumen yang ditemukan? [Y/N]\nJawab: ").upper()

    # Jika Y, maka akan masuk ke kondisi ini
    if moreinfo == "Y":
        print("\n" + "—"*125 + "\n")
        # Looping validasi input
        while True:
            try:
                # Input user untuk memilih dokumen yang akan dilihat
                docnum = int(input(f"Pilih nomor dokumen yang akan dilihat! (1-{counter})\nJawab: "))
                # Menyiapkan file path file XML yang akan dibuka
                file_path = os.path.join(folder_path, docnums[docnum-1])
                # Membuka dan mengambil isi file XML ke dalam variabel
                with open(file_path, 'r', encoding='utf-8') as file:
                    contents_raw = file.read()
                # Mendapatkan informasi dari header file XML
                amar = get_info("amar")
                amar_lainnya = get_info("amar_lainnya")
                id = get_info("id")
                klasifikasi = get_info("klasifikasi")
                lama_hukuman = get_info("lama_hukuman")
                lembaga_peradilan = get_info("lembaga_peradilan")
                provinsi = get_info("provinsi")
                status = get_info("status")
                sub_klasifikasi = get_info("sub_klasifikasi")
                url = get_info("url")
                # Print hasil informasi yang didapat
                print("\n" + "—"*125 + "\n" +
                        col_out("\nNama file: ") + docnums[docnum - 1] +
                        col_out("\nAmar: ") + amar +
                        col_out("\nAmar Lainnya: ") + amar_lainnya +
                        col_out("\nID: ") + id +
                        col_out("\nKlasifikasi: ") + klasifikasi +
                        col_out("\nLama Hukuman: ") + lama_hukuman +
                        col_out("\nLembaga Peradilan: ") + lembaga_peradilan +
                        col_out("\nProvinsi: ") + provinsi +
                        col_out("\nStatus: ") + status +
                        col_out("\nSub Klasifikasi: ") + sub_klasifikasi +
                        col_out("\nURL: ") + url
                        + "\n\n" + "—"*125 + "\n")
                break
            # Error handling jika input bukan angka
            except (ValueError, IndexError):
                print(col_warn("Input tidak valid!\n"))
                continue

    # Jika N, maka akan keluar program
    elif moreinfo == "N":
        print("\nTerimakasih sudah menggunakan program ini!\n")
        sys.exit()

    # Error handling jika input bukan Y atau N
    else:
        print(col_warn("Input tidak valid!\n"))
        continue


# =================================== END OF PROGRAM ===================================