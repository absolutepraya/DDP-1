import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.dict_hotel = {'Hotel 1': [10, 250000, 'kode_hotel_1'],
            'Hotel 2': [12, 500000, 'kode_hotel_2'],
            'Hotel 3': [10, 7500000, 'kode_hotel_3'],
            'Hotel 4': [1, 1000000, 'kode_hotel_4'],
            'Hotel 5': [10, 900000, 'kode_hotel_5'],
            'Hotel 6': [10, 6000000, 'kode_hotel_6'],
            'Hotel 7': [10, 6000000, 'kode_hotel_7'],
            'Hotel 8': [10, 6000000, 'kode_hotel_8'],
            'Hotel 9': [10, 6000000, 'kode_hotel_9'],
            'Hotel 10': [10, 6000000, 'kode_hotel_10'],
            'Hotel 11': [10, 6000000, 'kode_hotel_11'],
            'Hotel 12': [10, 6000000, 'kode_hotel_12'],
            'Hotel 13': [10, 6000000, 'kode_hotel_13'],
            'Hotel 14': [10, 6000000, 'kode_hotel_14'],
            'Hotel 15': [10, 6000000, 'kode_hotel_15'],
            'Hotel 16': [10, 6000000, 'kode_hotel_16'],
            'Hotel 17': [10, 6000000, 'kode_hotel_17'],
            'Hotel 18': [10, 6000000, 'kode_hotel_18'],
            'Hotel 19': [10, 6000000, 'kode_hotel_19'],
            'Hotel 20': [10, 6000000, 'kode_hotel_20']}

        # Set title dan ukuran windows, dan buat ukuran window tidak dapat diubah
        self.master.title("Paciloka App")
        self.master.geometry("820x600")
        self.master.resizable(False, False)

        bgcolor = "#0802A3"

        # Set background window
        self.master.configure(background=bgcolor)

        # Tambahkan teks selamat datang di bagian tengah atas window
        welcome_label = tk.Label(self.master, text="Selamat datang di Paciloka!", font=('Helvetica', 20, 'bold'), fg='white', bg=bgcolor)
        welcome_label.pack(pady=10)

        # Warna latar belakang canvas
        global canvas_bg_color
        canvas_bg_color = "#ffffff"

        # Tambahkan widget Canvas dan Scrollbar
        self.canvas = tk.Canvas(self.master, borderwidth=0, background=canvas_bg_color)
        
        # Buat frame baru untuk scrollbar
        scrollbar_frame = tk.Frame(self.master, bg=bgcolor)
        
        self.scrollbar = tk.Scrollbar(scrollbar_frame, orient="vertical", command=self.canvas.yview, bg=bgcolor)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pasang widget Canvas di tengah
        self.canvas.pack(side="left", fill="both", expand=True, padx=(10, 0))
        
        # Pasang scrollbar di sebelah kiri canvas
        self.scrollbar.pack(side="left", fill="y")
        
        # Pasang frame scrollbar di sebelah kiri canvas
        scrollbar_frame.pack(side="left", fill="y")
        
        # Buat frame sebagai anak dari widget Canvas
        self.frame = tk.Frame(self.canvas, background=canvas_bg_color)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Panggil fungsi untuk menambahkan elemen-elemen ke dalam frame
        self.homepage()

        # Kaitkan fungsi pada event resize window untuk mengatur ukuran tampilan di dalam canvas
        self.master.bind("<Configure>", self.on_frame_configure)

    # Menambahkan label, field, dan button yang dibutuhkan
    def homepage(self):
        for i in range(len(self.dict_hotel)):
            # Membuat frame untuk setiap hotel dengan border color dan ketebalan yang diinginkan
            hotel_frame = tk.Frame(self.frame, borderwidth=2, relief=tk.GROOVE, background="#ffffff", bd=3)

            # Menentukan kolom untuk frame (kiri atau kanan)
            column = i % 2
            hotel_frame.grid(row=i // 2, column=column, padx=10, pady=10, sticky="ew")

            # Menambahkan label-label ke dalam frame
            label1 = tk.Label(hotel_frame, text=f"Nama Hotel: {list(self.dict_hotel.keys())[i]}", font=('Helvetica', 12), background="#ffffff")
            label2 = tk.Label(hotel_frame, text=f"Jumlah Kamar Tersedia: {self.dict_hotel[list(self.dict_hotel.keys())[i]][0]}", font=('Helvetica', 12), background="#ffffff")
            label3 = tk.Label(hotel_frame, text=f"Harga per Kamar: {self.dict_hotel[list(self.dict_hotel.keys())[i]][1]}", font=('Helvetica', 12), background="#ffffff")

            # Dimasukkan ke dalam frame
            label1.grid(row=0, column=0, pady=5, sticky="w")
            label2.grid(row=1, column=0, pady=5, sticky="w")
            label3.grid(row=2, column=0, pady=5, sticky="w")

        # Buat frame baru untuk elemen-elemen di sebelah kanan canvas pertama
        right_frame = tk.Frame(self.master, background=canvas_bg_color)
        right_frame.pack(side="left", fill="y", padx=10)

        # Label masukkan data diri
        label_masukkan_data_diri = tk.Label(right_frame, text="Mau menginap di mana?", font=('Helvetica', 14, 'bold'), background="#ffffff")
        label_masukkan_data_diri.grid(row=0, column=0, pady=10, padx=20)

        # Label nama
        label_nama = tk.Label(right_frame, text="Nama Pengguna:", font=('Helvetica', 12), background="#ffffff")
        label_nama.grid(row=1, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field nama
        self.field_nama = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_nama.grid(row=2, column=0, pady=5, sticky="w", padx=(10, 0))

        # Label nama hotel
        label_nama_hotel = tk.Label(right_frame, text="Nama Hotel:", font=('Helvetica', 12), background="#ffffff")
        label_nama_hotel.grid(row=3, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field nama hotel
        self.field_nama_hotel = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_nama_hotel.grid(row=4, column=0, pady=5, sticky="w", padx=(10, 0))

        # Label jumlah kamar
        label_jumlah_kamar = tk.Label(right_frame, text="Jumlah Kamar:", font=('Helvetica', 12), background="#ffffff")
        label_jumlah_kamar.grid(row=5, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field jumlah kamar
        self.field_jumlah_kamar = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_jumlah_kamar.grid(row=6, column=0, pady=5, sticky="w", padx=(10, 0))

        # Label kode promo
        label_promo = tk.Label(right_frame, text="Kode Promo:", font=('Helvetica', 12), background="#ffffff")
        label_promo.grid(row=7, column=0, pady=5, sticky="w", padx=(10, 0))
        # Field kode promo
        self.field_promo = tk.Entry(right_frame, width=20, font=('Arial', 12))
        self.field_promo.grid(row=8, column=0, pady=5, sticky="w", padx=(10, 0))

        # Tombol untuk menampilkan window baru yang mencetak daftar kode promo yang tersedia
        button_promo = tk.Button(right_frame, text="Cek Promo", font=('Helvetica', 12, 'bold',), command=self.show_promo, background="#f2bf04")
        button_promo.grid(row=9, column=0, pady=5, sticky="w", padx=(10, 0))
        
        # Tombol pesan kamar
        button_pesan = tk.Button(right_frame, text="Pesan Kamar", font=('Helvetica', 12, 'bold'), command=self.booking, width=20, background="#0e72ff", fg="#ffffff")
        button_pesan.grid(row=10, column=0, pady=(35, 5))

        # Tombol exit
        button_exit = tk.Button(right_frame, text="Exit", font=('Helvetica', 12, 'bold'), command=self.master.destroy, width=20, background="#ed3838", fg="#ffffff")
        button_exit.grid(row=11, column=0, pady=5)

    # Fungsi yang dipanggil saat ukuran frame diubah
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    # Fungsi untuk menampilkan window promo
    def show_promo(self):
        # Buat window baru
        promo_window = tk.Toplevel(self.master)
        promo_window.title("Kode Promo")
        promo_window.geometry("300x350")
        promo_window.resizable(False, False)

        # Set background window
        promo_window.configure(background=canvas_bg_color)

        # Label daftar promo code
        label_promo = tk.Label(promo_window, text="Daftar Kode Promo", font=('Helvetica', 14, 'bold'), background="#ffffff")
        label_promo.pack(pady=(20, 0))

        # Daftar kode promo
        promo_codes = {'FLYAWAY25': [r'25% off every Friday', 0.25, 'percentage'],
                    'STAYTILL20': [r'Rp200.000 off until 20 Dec', -200000, 'fixed'],
                    'EID40': [r'40% off during Eid holiday', 0.4, 'percentage'],
                    'PACILOKA24': [r'Rp240.000 off if you are a Pacilian', -240000, 'fixed']}
        
        # Mencetak daftar kode promo tanpa menggunakan frame box dengan looping, dengan format:
        # <Kode Promo> (Bold Italic)
        # <Deskripsi>

        for code, desc in promo_codes.items():
            # Pencetakan kode promo
            label_code = tk.Label(promo_window, text=f"{code}", font=('Helvetica', 12, 'bold italic'), background="#ffffff")
            label_desc = tk.Label(promo_window, text=f"{desc[0]}", font=('Helvetica', 12), background="#ffffff")

            # Peletakkan kode promo
            label_code.pack(pady=(15, 0), padx=10, anchor="w")
            label_desc.pack(pady=3, padx=10, anchor="w")

    
    # Fungsi utama dalam operasi pemesanan kamar hotel
    def booking(self):
        # Konversi input field ke tipe yang diinginkan
        nama = str(self.field_nama.get())
        nama_hotel = str(self.field_nama_hotel.get())
        jumlah_kamar = int(self.field_jumlah_kamar.get())
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
        elif kode == "":
            total_harga = jumlah_kamar * hotel[1]
        else:
            messagebox.showerror("Error", "Kode promo tidak ada!")
            return

        # Tampilkan informasi pemesanan
        messagebox.showinfo("Order confirmed!",
                            "Booking berhasil!\n" +
                            f"Pesanan untuk {nama} di {nama_hotel} sebanyak {jumlah_kamar}!\n" + 
                            f"Total biaya: {total_harga}\n" +
                            f"Nomor tiket: {hotel[2]}/{jumlah_kamar}/{nama[:3]}")
        
        # Update jumlah kamar yang tersedia
        self.dict_hotel[nama_hotel][0] -= jumlah_kamar

        # Mengosongkan field-field yang sudah diisi
        self.field_nama.delete(0, tk.END)
        self.field_nama_hotel.delete(0, tk.END)
        self.field_jumlah_kamar.delete(0, tk.END)
        self.field_promo.delete(0, tk.END)

        # Update tampilan
        

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
