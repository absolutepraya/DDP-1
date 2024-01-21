# Recursive function untuk mengisi input
def recursive_input(inp=[]):
    input_str = input()
    # Base case
    if input_str.upper() == "SELESAI":
        return inp
    input_str = input_str.split(" ")
    inp.append([input_str[0], input_str[1]])
    # Recursive call
    return recursive_input(inp)

# (MENU 1) Recursive function untuk memeriksa keturunan, apakah child merupakan keturunan dari parent
def cek_keturunan(tree, parent, child):
    for a in tree[parent]:
        # Base case
        if a == child:
            return True
        # Recursive call
        else:
            if a in tree.keys() and cek_keturunan(tree, a, child):
                return True
    # Jika tidak return True selama loop, maka return False
    return False

# (MENU 2) Recursive function untuk mencetak semua child dari parent, baik itu child langsung maupun tidak langsung
def cetak_keturunan(tree, parent):
    # Base case menggunakan if, jika tidak memenuhi, maka akan skipped
    if parent in tree:
        direct_childs = tree[parent]
        print('- ' + ' '.join(direct_childs))
        # Recursive call
        for child in direct_childs:
            cetak_keturunan(tree, child)

# (MENU 3) Recursive function untuk mencari jarak generasi antara dua orang
def jarak_generasi(tree, parent, child, distance=1):
    for a in tree[parent]:
        # Base case
        if a == child:
            return distance
        else:
            # Recursive call
            if a in tree.keys() and cek_keturunan(tree, a, child):
                return jarak_generasi(tree, a, child, distance + 1)

# Meminta input data relasi
print("Masukkan data relasi:")
input_lst = recursive_input()

# Loop untuk mengubah input ke dalam bentuk dictionary
family_tree = {}
for parent, child in input_lst:
    if parent not in family_tree:
        family_tree[parent] = []
    family_tree[parent].append(child)


# ————————————————————————————— MAIN PROGRAM —————————————————————————————


# Loop utama program
while True:
    # Mencetak pilihan menu
    print(family_tree)
    print("\n=====================================================================" +
        "\nSelamat Datang di Relation Finder! Pilihan yang tersedia:" +
        "\n1. CEK_KETURUNAN" +
        "\n2. CETAK_KETURUNAN" +
        "\n3. JARAK_GENERASI" +
        "\n4. EXIT")
    menu = input("Masukkan pilihan: ")

    # Menu pilihan 1
    if menu == "1":
        # Meminta input nama parent dan child
        person1 = input("Masukkan nama parent: ")
        person2 = input("Masukkan nama child: ")
        # Memeriksa apakah person1 dan person2 sama, apakah person1 ada di dalam family_tree
        if person1 == person2 or person1 not in family_tree:
            print(f"{person2} bukan merupakan keturunan dari {person1}")
        elif cek_keturunan(family_tree, person1, person2):
            print(f"{person2} benar merupakan keturunan dari {person1}")
        else:
            print(f"{person2} bukan merupakan keturunan dari {person1}")
    
    # Menu pilihan 2
    elif menu == "2":
        # Meminta input nama parent
        person = input("Masukkan nama parent: ")
        # Langsung memanggil fungsi cetak_keturunan, jika parent tidak ada, maka outputnya kosong
        cetak_keturunan(family_tree, person)

    # Menu pilihan 3
    elif menu == "3":
        # Meminta input nama parent dan child
        person1 = input("Masukkan nama parent: ")
        person2 = input("Masukkan nama child: ")
        # Memeriksa apakah person1 dan person2 sama
        if person1 == person2:
            print(f"{person1} memiliki hubungan dengan {person2} sejauh 0")
        # Memanggil fungsi
        elif cek_keturunan(family_tree, person1, person2):
            print(f"{person1} memiliki hubungan dengan {person2} sejauh {jarak_generasi(family_tree, person1, person2)}")
        # Jika tidak ada hubungan, maka tidak ada hubungan
        else:
            print(f"Tidak ada hubungan antara {person1} dengan {person2}")
        
    # Menu pilihan 4, keluar program
    elif menu == "4":
        print("=====================================================================" +
            "\nTerima kasih telah menggunakan Relation Finder!")
        break