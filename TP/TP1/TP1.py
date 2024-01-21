import turtle
import math # Untuk mempermudah membuat kepala Super Mushroom Mario

# Mendefine 'bob' sebagai nama turtle karena lucu & 'screen' sebagai screen output turtle
bob = turtle.Turtle()
screen = turtle.Screen()

# Tujuannya agar window output turtle ter-maximize
screen.setup(width=1.0, height=1.0)

# Mempercepat gerak turtle
bob.speed(0)
turtle.delay(0)

turtle.screensize(10000, 10000)


# =============== INPUT VALUE UNTUK MEMBUAT TOWER  ===============


# Validasi input jumlah tower yang akan dibuat dengan minimum nilainya adalah 1
tower = int(bob.screen.numinput("Tower to Build", "Enter the amount of tower you want to build (integer)", 
        minval = 1))

# Conditionals jumlah tower
if tower == 1:
    # Menyatakan value distance & difference di angka 0 karena tidak perlu dihitung
    distance = 0
    difference = 0
else:
    # Validasi input jarak antara tower dengan minimum nilai 2 dan maksimum nilai 5
    distance = int(bob.screen.numinput("Distance between Towers", "Enter the distance between towers (integer)",
                minval = 2, maxval = 5))
    # Validasi input perbedaan jumlah tumpukan layer antara tower dengan minimum nilai 2 dan maksimum nilai 5
    difference = int(bob.screen.numinput("Tower Layer Difference", "Enter the number of layer difference between each tower (integer)", 
                minval = 2, maxval = 5))

# Validasi input lebar batu bata dengan maksimum 35 pixel
brick_hor = int(bob.screen.numinput("Brick Width", "Enter the width of the brick (integer)", 
            minval = 1, maxval = 35))

# Validasi input tinggi batu bata dengan maksimum 25 pixel
brick_ver = int(bob.screen.numinput("Brick Height", "Enter the height of the brick (integer)", 
            minval = 1, maxval = 25))

# Validasi input jumlah tumpukan layer tower pertama dengan maksimum 25 batu bata
layer_ver = int(bob.screen.numinput("First Tower Layer Amount", "Enter the amount of layer for the first tower (integer)", 
            minval = 1, maxval = 25))

# Validasi input panjang layer tower dengan maksimum 10 batu bata
layer_hor = int(bob.screen.numinput("Layer Length", "Enter the length of the layer (integer)", 
            minval = 1, maxval = 10))

"""Mendefine titik 0 sumbu-x dan titik 0 sumbu-y di screen turtle,
untuk kemudian ditambahkan di setiap statement goto()"""
start_x = -1 * 1/2 * (layer_hor + distance) * brick_hor * tower # Centering sesuai panjang horizontal output
start_y = -275


# ========================= MAIN PROGRAM =========================


# For loop untuk setiap tower
for i in range(tower):
    
    # Warna badan tower
    bob.color("black", "#CA7F65")

    if (i + 1) % 3 == 0:
        bob.color("black", "red")

    bob.penup()

    # Deine variable untuk fungsi goto()
    lebar_tower = layer_hor * brick_hor
    jarak_antar_tower = (layer_hor + distance) * brick_hor
    tinggi_tower = (layer_ver + difference * i) * brick_ver
    tinggi_tower_atap = (layer_ver + 1 + difference * i) * brick_ver

    # Memindahkan turtle ke pojok kiri bawah setiap tower yang akan dibuat
    bob.goto(start_x + i * jarak_antar_tower, start_y + 0)
    
    bob.pendown()

    # Membuat bentuk kotak utama tower
    bob.begin_fill()
    for j in range(2):
        bob.forward(lebar_tower)
        bob.left(90)
        bob.forward(tinggi_tower)
        bob.left(90)
    bob.end_fill()

    # Membuat batu batanya (horizontal)
    for j in range(1, layer_ver + (difference * i)):
        bob.goto(start_x + i * jarak_antar_tower, start_y + j * brick_ver)
        bob.pendown()
        bob.forward(lebar_tower)
        bob.penup()

    bob.left(90)

    # Membuat batu batanya (vertikal)
    for j in range(1, layer_hor):
        bob.goto(start_x + i * jarak_antar_tower + j * brick_hor, start_y + 0)
        bob.pendown()
        bob.forward(tinggi_tower)
        bob.penup()

    bob.right(90)

    # Warna bagian atas tower
    bob.color("black", "#693424")

    # Memindahkan turtle ke bagian kiri atas tower (lebih 1/2 batu bata)
    bob.goto(start_x + i * jarak_antar_tower - 1/2 * brick_hor, start_y + tinggi_tower)

    # Membuat bentuk kotak bagian atas tower
    bob.begin_fill()
    for j in range(2):
        bob.pendown()
        bob.forward((layer_hor + 1) * brick_hor)
        bob.left(90)
        bob.forward(brick_ver)
        bob.left(90)
        bob.penup()
    bob.end_fill()

    # Membuat batu batanya
    for j in range(1, layer_hor + 1):
        bob.forward(brick_hor)
        bob.left(90)
        bob.pendown()
        bob.forward(brick_ver)
        bob.penup()
        bob.back(brick_ver)
        bob.right(90)
    
    # Warna bagian badan Super Mushroom
    bob.color("black", "#FCCFAD") # Beige

    # Memindahkan turtle tepat di atas bagian atas tower, dan tepat di tengah
    bob.goto(start_x + i * jarak_antar_tower + 1/2 * lebar_tower, start_y + tinggi_tower_atap)

    bob.pendown()

    # Membuat bentuk kotak bagian badan Super Mushroom sesuai ukuran tower
    bob.begin_fill()
    for j in range(2):
        bob.forward(0.6 * brick_hor)
        bob.left(90)
        bob.forward(0.6 * brick_hor)
        bob.left(90)
        bob.forward(0.6 * brick_hor)
    bob.end_fill()

    bob.penup()

    # Warna topi Super Mushroom
    bob.color("black", "#ED212C") # Red

    # Memindahkan turtle tepat di atas badan Super Mushroom, dan tepat di tengah
    bob.goto(start_x + i * jarak_antar_tower + 1/2 * lebar_tower, start_y + tinggi_tower_atap + 2.3 * brick_hor)

    bob.pendown()

    """
    Membuat bentuk topi Super Mushroom sesuai ukuran tower dengan cara membuat 260 derajat lingkaran.
    1) Membuat lingkaran ke arah kanan bawah
    Turtle harus mengarah ke kiri dan melakukan gerak mundur (negatif)
    2) Membuat garis yang ditarik antara kedua titik di dalam lingkaran
    Menggunakan rumus 2*jari-jari*sin(t/2)
    3) Membuat lingkaran ke arah kanan atas
    Turtle harus mengarah ke kiri bawah dan melakukan gerak mundur (negatif)
    """
    bob.begin_fill()
    bob.left(180)
    bob.circle(1.1 * brick_hor, -130)
    bob.left(130)
    bob.forward(2 * 1.1 * brick_hor * math.sin(math.radians(260)/2)) # Rumus = 2*jari-jari*sin(t/2) dengan t harus dalam bentuk radian
    bob.left(130)
    bob.circle(1.1 * brick_hor, -130)
    bob.left(180)
    bob.end_fill()

    bob.penup()

    # Set warna mata Super Mushroom
    bob.color("black", "black")
    bob.pensize(0.2 * brick_hor) # Menebalkan pensize sesuai ukuran tower

    # Memindahkan turtle ke bagian kiri atas badan Super Mushroom
    bob.goto(start_x + i * jarak_antar_tower + 1/2 * lebar_tower - 1/4 * brick_hor, start_y + tinggi_tower_atap + 0.3 * 1.2 * brick_hor)

    bob.pendown()
    bob.right(90)

    # Membuat mata kiri Super Mushroom
    bob.forward(0.1 * brick_hor)

    bob.penup()

    # Memindahkan turtle ke bagian kanan atas badan Super Mushroom
    bob.goto(start_x + i * jarak_antar_tower + 1/2 * lebar_tower + 1/4 * brick_hor, start_y + tinggi_tower_atap + 0.3 * 1.2 * brick_hor)

    bob.pendown()

    # Membuat mata kanan Super Mushroom
    bob.forward(0.1*brick_hor)

    bob.penup()
    bob.left(90)

    bob.pensize(1) # Mengembalikan pensize ke bentuk semula

bob.left(90)

# Memindahkan turtle ke bagian bawah tower-tower yang sudah dibuat
bob.goto(-300, start_y + -120)

# Total batu bata yang digunakan menggunakan rumus Sn deret aritmatika
n = tower
a = layer_hor * layer_ver + layer_hor + 1
b = layer_hor * difference
total_bricks = n/2 * (2 * a + (n - 1) * b)

# Output total batu bata yang digunakan
bob.write(f"{tower} Super Mario Towers have been built with a total of {int(total_bricks)} bricks." +
        f"\nAnd also {tower} (game-accurate) Super Mushrooms have been spawned \non top of every tower.", 
        font=("Calibri", 17, "bold"))

turtle.done()


# ======================== END OF PROGRAM ========================