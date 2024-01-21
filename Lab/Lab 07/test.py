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

# (MENU 1) Recursive function untuk memeriksa keturunan
def check_family_tree(tree, parent, child):
    

# (MENU 2) Recursive function untuk mencetak semua child dari parent, baik itu child langsung maupun tidak langsung
def print_childs(tree, parent, level=0):
    if parent in tree:
        direct_childs = tree[parent]
        print('- ' + ' '.join(direct_childs))
        for child in direct_childs:
            print_childs(tree, child, level + 1)

# (MENU 3) Recursive function untuk mencari jarak generasi antara dua orang
def find_generation_distance(tree, person1, person2, distance=0):
    


input_lst = [['Asep', 'Dwi'], ['Agus', 'Budi'], ['Budi', 'Bambang'], ['Agus', 'Asep'], ['Budi', 'Fatalis']]

family_tree = {}

for parent, child in input_lst:
    if parent not in family_tree:
        family_tree[parent] = []
    family_tree[parent].append(child)

while True:
    print(family_tree)
    print("""
=====================================================================
Selamat Datang di Relation Finder! Pilihan yang tersedia:
1. CEK_KETURUNAN
2. CETAK_KETURUNAN
3. JARAK_GENERASI
4. EXIT""")
    menu = input("Masukkan pilihan: ")

    if menu == "1":
        person1 = input("Masukkan nama parent: ")
        person2 = input("Masukkan nama child: ")
        print(check_family_tree(family_tree, person1, person2))
    
    elif menu == "2":
        person = input("Masukkan nama parent: ")
        print_childs(family_tree, person)

    elif menu == "3":
        person1 = input("Masukkan nama parent: ")
        person2 = input("Masukkan nama child: ")
        print(find_generation_distance(family_tree, person1, person2))

    elif menu == "4":
        print("""
=====================================================================
Terima kasih telah menggunakan Relation Finder!""")
        break