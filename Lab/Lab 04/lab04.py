import sys

# ========================= FUNCTIONS ========================= #

# Function untuk mencetak header tabel
def print_headers():
    """
    Header tabel terdiri dari 5 kolom:
    1) nomor urut (No), 
    2) nama smartphone (Smartphone), 
    3) harga (Price), 
    4) ukuran layar (Screensize), dan 
    5) RAM.
    Setiap kolom memiliki spacing 2, 25, 8, 10, dan 3 karakter serta left-aligned
    """
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# Function untuk mencetak isi tabel secara keseluruhan dari file
def print_table(filename):
    """
    Cara kerja fungsi (ditandai dengan label #[NOMOR KERJA]):
    1. Buka file dengan mode read, dan memasukkan isi file ke variable contents dalam bentuk list.
    2. Mencetak header tabel.
    3. Looping untuk setiap baris di variable contents.
    4. Masuk ke dalam line ke-i, lalu di-split dengan separator tab agar menjadi list.
    5. Cetak isi tabel dengan format yang sudah ditentukan.
    """
    try:
        with open(filename, "r") as file: #1
            contents = file.readlines()
        print_headers() #2
        for i in range(len(contents)): #3
            line = contents[i].strip().split("\t") #4
            print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format((i + 1), line[0], line[1], line[2], line[3])) #5
    except FileNotFoundError: # Menangkap error jika file tidak ditemukan
        print("Maaf, file input tidak ada")
        sys.exit(1)

# Function untuk mencari smartphone berdasarkan keyword
def search_phone(filename, keyword):
    """
    Cara kerja fungsi (ditandai dengan label #[NOMOR KERJA]):
    1. Buka file dengan mode read, dan memasukkan isi file ke variable contents dalam bentuk list.
    2. Mencetak header tabel.
    3. Looping untuk setiap baris di variable contents.
    4. Masuk ke dalam line ke-i, lalu di-split dengan separator tab agar menjadi list.
    5. Jika keyword ada di dalam nama smarthphone, maka keyword counter + 1
    6. Cetak isi tabel dengan format yang sudah ditentukan.
    7. Print ukuran data = data yang ditemukan x banyak kolom.
    """
    print()
    with open(filename, "r") as file: #1
        contents = file.readlines()
    print_headers() #2
    # Keyfound untuk nomor urut & jumlah data yang ditemukan
    keyfound = 0  
    for i in range(len(contents)): #3
        line = contents[i].strip().split("\t") #4
        if keyword.lower() in line[0].lower():
            keyfound += 1 #5
            print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(keyfound, line[0], line[1], line[2], line[3])) #6
    print(f"Ukuran data dari hasil pencarian: {keyfound} x 4") #7

# Function untuk mencari statistik deskriptif dari data
"""
Cara kerja fungsi (ditandai dengan label #[NOMOR KERJA]):
1. Buka file dengan mode read, dan memasukkan isi file ke dalam variable contents dalam bentuk list.
2. Looping untuk setiap baris di variable contents.
3. Masuk ke dalam line ke-i, lalu di-split dengan separator tab agar menjadi list.
4. Append kolom yang diminta ke dalam list dataset.
5. Cetak nilai minimum, maximum, dan rata-rata dari data yang ada di dalam list dataset.
"""
def desc_stat(filename, column):
    with open(filename, "r") as file: #1
        contents = file.readlines()
    dataset = []
    for i in range(len(contents)): #2
        line = contents[i].strip().split("\t") #3
        dataset.append(float(line[column])) #4
    #5
    print(f"Min data: {min(dataset):.2f}")
    print(f"Max data: {max(dataset):.2f}")
    print(f"Rata - rata: {sum(dataset) / len(dataset):.2f}")

# ========================= MAIN PROGRAM ========================= #

if __name__ == '__main__':
    if len(sys.argv) != 4 or sys.argv[3] not in ["1", "2", "3"]:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)
    # Menyimpan argumen ke dalam variable
    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

# Memanggil fungsi yang sudah dibuat
print_table(file_path)
search_phone(file_path, key)
desc_stat(file_path, column_num)