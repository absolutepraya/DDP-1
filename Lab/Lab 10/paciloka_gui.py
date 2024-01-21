import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        # Daftar hotel yang tersedia beserta jumlah kamar, harga per kamar, dan kode tiketnya (base64 encoded)
        self.dict_hotel = {'Aston': [10, 250000, 'YXN0b24'],
            'MaxOne': [12, 500000, 'TWF4T25l'],
            'Artotel': [10, 7500000, 'QXJ0b3RlbA'],
            'Favehotel': [1, 1000000, 'RmF2ZQ'],
            'Ibis': [10, 900000, 'SWJpcw'],
            'Amaris': [45, 6000000, 'QW1hcmlz'],
            'Neo': [6, 700000, 'UE9QIQ'],
            'Whiz': [23, 1500000, 'TmVv'],
            'Zen': [17, 8900000, 'V2hpeg'],
            'RedDoorz': [25, 450000, 'UmVkRG9vcno'],
            'HARRIS': [25, 230000, 'SEFSUklT'],
            'Harper': [10, 450000, 'SGFwZXI'],
            'Alila': [34, 100000, 'QWxpbGE'],
            'Quest': [40, 6700000, 'U2VxdWV0'],
            'Intercon': [10, 4300000, 'U3dpc3MtQmVsaW5u'],
            'Kempinski': [20, 6000000, 'QXJ5YWR1dGE'],
            'Gaia': [21, 650000, 'WmVu'],
            'Mercure': [3, 2400000, 'SGFycmlz']}

        # Set title dan ukuran windows, dan buat ukuran window tidak dapat diubah
        self.master.title("Paciloka App")
        self.master.geometry("820x600")
        self.master.resizable(False, False)

        # Warna latar belakang window
        global bgcolor
        bgcolor = "#0802A3"
        self.master.configure(background=bgcolor)

        # Tambahkan teks selamat datang di bagian tengah atas window
        welcome_label = tk.Label(self.master, text="Selamat datang di Paciloka! 🕊️", font=('Arial', 20, 'bold'), fg='white', bg=bgcolor)
        welcome_label.pack(pady=10)

        # Warna latar belakang canvas
        global canvas_bg_color
        canvas_bg_color = "#ffffff"

        # Panggil fungsi untuk menampilkan elemen-elemen di dalam frame
        self.mainpage()

        # Kaitkan fungsi pada event resize window untuk mengatur ukuran tampilan di dalam canvas
        self.master.bind("<Configure>", self.on_frame_configure)

    def mainpage(self):
        # Tambahkan widget Canvas dan Scrollbar
        self.canvas = tk.Canvas(self.master, borderwidth=0, background=canvas_bg_color)
        
        # Buat frame baru untuk scrollbar
        scrollbar_frame = tk.Frame(self.master, bg=bgcolor)
        
        # Tambahkan scrollbar vertikal
        self.scrollbar = tk.Scrollbar(scrollbar_frame, orient="vertical", command=self.canvas.yview, bg=bgcolor)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pasang widget Canvas di kiri window
        self.canvas.pack(side="left", fill="both", expand=True, padx=(10, 0))
        
        # Pasang scrollbar dan framenya di sebelah kiri canvas
        self.scrollbar.pack(side="left", fill="y")
        scrollbar_frame.pack(side="left", fill="y")
        
        # Buat frame sebagai inheritance dari widget Canvas
        self.frame = tk.Frame(self.canvas, background=canvas_bg_color)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Panggil fungsi untuk menambahkan elemen-elemen ke dalam frame
        self.homepage()

    # Menambahkan label, field, dan button yang dibutuhkan
    def homepage(self):
        for i in range(len(self.dict_hotel)):
            # Membuat frame untuk setiap hotel dengan border color dan ketebalan yang diinginkan
            hotel_frame = tk.Frame(self.frame, borderwidth=2, relief=tk.GROOVE, background="#ffffff", bd=3)

            # Menentukan kolom untuk frame (kiri atau kanan)
            column = i % 2

            # Memasuukan frame ke dalam canvas
            hotel_frame.grid(row=i // 2, column=column, padx=10, pady=10, sticky="ew")

            # Menambahkan label nama hotel, jumlah kamar, dan harga per kamar
            label1 = tk.Label(hotel_frame, text=f"Nama Hotel: {list(self.dict_hotel.keys())[i]}", font=('Arial', 12), background="#ffffff")
            label2 = tk.Label(hotel_frame, text=f"Jumlah Kamar Tersedia: {self.dict_hotel[list(self.dict_hotel.keys())[i]][0]}", font=('Arial', 12), background="#ffffff")
            label3 = tk.Label(hotel_frame, text=f"Harga per Kamar: {self.dict_hotel[list(self.dict_hotel.keys())[i]][1]}", font=('Arial', 12), background="#ffffff")

            # Memasukkan label ke dalam frame menggunakan grid
            label1.grid(row=0, column=0, pady=5, sticky="w")
            label2.grid(row=1, column=0, pady=5, sticky="w")
            label3.grid(row=2, column=0, pady=5, sticky="w")

        # Buat frame baru untuk elemen-elemen di sebelah kanan canvas pertama
        right_frame = tk.Frame(self.master, background=canvas_bg_color)
        right_frame.pack(side="left", fill="y", padx=10)

        # Label masukkan data diri
        label_menginap = tk.Label(right_frame, text="Mau menginap di mana? ", font=('Arial', 14, 'bold'), background="#ffffff")
        label_menginap.grid(row=0, column=0, pady=10, padx=20)

        # Label nama
        label_nama = tk.Label(right_frame, text="Nama Pengguna:", font=('Arial', 12), background="#ffffff")
        label_nama.grid(row=1, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field nama
        self.field_nama = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_nama.grid(row=2, column=0, pady=5, sticky="w", padx=(10, 0))

        # Label nama hotel
        label_nama_hotel = tk.Label(right_frame, text="Nama Hotel:", font=('Arial', 12), background="#ffffff")
        label_nama_hotel.grid(row=3, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field nama hotel
        self.field_nama_hotel = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_nama_hotel.grid(row=4, column=0, pady=5, sticky="w", padx=(10, 0))

        # Label jumlah kamar
        label_jumlah_kamar = tk.Label(right_frame, text="Jumlah Kamar:", font=('Arial', 12), background="#ffffff")
        label_jumlah_kamar.grid(row=5, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field jumlah kamar
        self.field_jumlah_kamar = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_jumlah_kamar.grid(row=6, column=0, pady=5, sticky="w", padx=(10, 0))

        # Label kode promo
        label_promo = tk.Label(right_frame, text="Kode Promo:", font=('Arial', 12), background="#ffffff")
        label_promo.grid(row=7, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field kode promo
        self.field_promo = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_promo.grid(row=8, column=0, pady=5, sticky="w", padx=(10, 0))

        # Tombol untuk menampilkan window baru yang mencetak daftar kode promo yang tersedia
        button_promo = tk.Button(right_frame, text="Cek Promo", font=('Arial', 12, 'bold',), command=self.show_promo, background="#f2bf04")
        button_promo.grid(row=9, column=0, pady=5, sticky="w", padx=(10, 0))
        
        # Tombol pesan kamar
        button_pesan = tk.Button(right_frame, text="Pesan Kamar", font=('Arial', 12, 'bold'), command=self.booking, width=20, background="#0e72ff", fg="#ffffff")
        button_pesan.grid(row=10, column=0, pady=(35, 5))

        # Tombol exit
        button_exit = tk.Button(right_frame, text="Exit", font=('Arial', 12, 'bold'), command=self.master.destroy, width=20, background="#ed3838", fg="#ffffff")
        button_exit.grid(row=11, column=0, pady=5)

    # Fungsi yang dipanggil saat ukuran frame diubah
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    # Fungsi untuk menampilkan window promo
    def show_promo(self):
        # Buat window baru yang menampilkan daftar kode promo, dan atur ukuran window agar tidak dapat diubah
        promo_window = tk.Toplevel(self.master)
        promo_window.title("Kode Promo")
        promo_window.geometry("300x350")
        promo_window.resizable(False, False)

        # Set background window
        promo_window.configure(background=canvas_bg_color)

        # Label daftar promo code
        label_promo = tk.Label(promo_window, text="Daftar Kode Promo", font=('Arial', 14, 'bold'), background="#ffffff")
        label_promo.pack(pady=(20, 0))

        # Daftar kode promo
        promo_codes = {'FLYAWAY25': [r'25% off every Friday', 0.25, 'percentage'],
                    'STAYTILL20': [r'Rp200.000 off until 20 Dec', -200000, 'fixed'],
                    'EID40': [r'40% off during Eid holiday', 0.4, 'percentage'],
                    'PACILOKA24': [r'Rp240.000 off if you are a Pacilian', -240000, 'fixed']}

        # Pencetakan kode promo
        for code, desc in promo_codes.items():
            # Membuat label untuk setiap kode promo
            label_code = tk.Label(promo_window, text=f"{code}", font=('Arial', 12, 'bold italic'), background="#ffffff")
            label_desc = tk.Label(promo_window, text=f"{desc[0]}", font=('Arial', 12), background="#ffffff")

            # Peletakkan kode promo
            label_code.pack(pady=(15, 0), padx=10, anchor="w")
            label_desc.pack(pady=3, padx=10, anchor="w")
    
    # Fungsi utama dalam operasi pemesanan kamar hotel
    def booking(self):
        # Konversi input field ke tipe yang diinginkan
        nama = str(self.field_nama.get())
        nama_hotel = str(self.field_nama_hotel.get())
        # Cek apakah jumlah kamar bukan berupa angka
        try:
            jumlah_kamar = int(self.field_jumlah_kamar.get())
            # Cek apakah jumlah kamar kurang dari 1
            if jumlah_kamar < 1:
                messagebox.showerror("Error", "Maaf, kamar yang dipesan harus lebih dari 0!")
                return
        except ValueError:
            messagebox.showerror("Error", "Jumlah kamar harus berupa angka!")
            return
        kode = str(self.field_promo.get())

        # Mendapatkan info hotel yang dipilih
        hotel = self.dict_hotel[nama_hotel]

        # Cek apakah hotel yang dipilih ada di daftar hotel
        if nama_hotel not in self.dict_hotel.keys():
            messagebox.showerror("Error", f"Maaf, {nama_hotel} tidak tersedia di sistem.")
            return

        # Cek apakah kamar hotel lebih dari 0
        if hotel[0] <= 0:
            messagebox.showerror("Error", "Kamar hotel sudah habis!")
            return
        
        # Cek apakah jumlah kamar yang diminta melebihi jumlah kamar yang tersedia
        if jumlah_kamar > hotel[0]:
            messagebox.showerror("Error", "Jumlah kamar yang diminta melebihi jumlah kamar yang tersedia!")
            return
        
        # Cek apakah jumlah kamar yang diminta kurang dari 1
        if jumlah_kamar < 1:
            messagebox.showerror("Error", "Jumlah kamar yang diminta minimal 1!")
            return
        
        # Hitung total harga jika menggunakan promo code
        if kode == "FLYAWAY25":
            total_harga = jumlah_kamar * hotel[1] * (1 - 0.25)
        elif kode == "STAYTILL20":
            total_harga = jumlah_kamar * hotel[1] - 200000
        elif kode == "EID40":
            total_harga = jumlah_kamar * hotel[1] * (1 - 0.4)
        elif kode == "PACILOKA24":
            total_harga = jumlah_kamar * hotel[1] - 240000
        # Jika tidak menggunakan promo code
        elif kode == "":
            total_harga = jumlah_kamar * hotel[1]
        # Jika menggunakan promo code yang tidak ada di daftar promo code
        else:
            messagebox.showerror("Error", "Kode promo tidak ada!")
            return

        # Tampilkan informasi pemesanan
        messagebox.showinfo("Order confirmed!",
                            "Booking berhasil!\n" +
                            f"Pesanan untuk {nama} di {nama_hotel} sebanyak {jumlah_kamar}!\n" + 
                            f"Total biaya: Rp{int(total_harga)}\n" +
                            f"Nomor tiket: {hotel[2]}/{jumlah_kamar}/{nama[:3]}")
        
        # Update jumlah kamar yang tersedia
        self.dict_hotel[nama_hotel][0] -= jumlah_kamar

        # Menghapus canvas pertama dan widget-widget yang ada di dalamnya
        self.canvas.destroy()
        self.frame.destroy()
        self.scrollbar.destroy()

        # Menghapus semua label, entry field, dan button yang ada di sebelah kanan canvas pertama
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

        # Mengulang proses yang sama untuk membuat canvas baru
        self.mainpage()

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()