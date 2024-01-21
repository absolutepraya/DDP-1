import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.dict_hotel = {'hotel1': [10, 250000, 'kode_hotel_1'],
                           'hotel2': [12, 500000, 'kode_hotel_2'],
                           'hotel3': [10, 7500000, 'kode_hotel_3'],
                           'hotel4': [1, 1000000, 'kode_hotel_4'],
                           'hotel5': [10, 900000, 'kode_hotel_5'],
                           'hotel6': [10, 6000000, 'kode_hotel_6']}

        # Set title dan ukuran windows
        self.master.title("Paciloka App")

        # Tambahkan teks selamat datang di bagian tengah atas window
        welcome_label = tk.Label(self.master, text="Selamat datang di Paciloka!", font=('Helvetica', 16, 'bold'))
        welcome_label.pack(pady=10)

        # Warna latar belakang canvas
        canvas_bg_color = "#ffffff"

        # Tambahkan widget Canvas dan Scrollbar
        self.canvas = tk.Canvas(self.master, borderwidth=0, background=canvas_bg_color)
        self.scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pasang widget Canvas di tengah
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Buat frame sebagai anak dari widget Canvas
        self.frame = tk.Frame(self.canvas, background=canvas_bg_color)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Panggil fungsi untuk menambahkan elemen-elemen ke dalam frame
        self.homepage()

        # Kaitkan fungsi pada event resize window untuk mengatur ukuran tampilan di dalam canvas
        self.master.bind("<Configure>", self.on_frame_configure)

        # Atur tinggi window sesuai dengan tinggi maksimum widget
        self.master.update_idletasks()  # Memastikan widget sudah tampil sepenuhnya
        self.master.geometry(f"800x{self.frame.winfo_reqheight()}")

    # Menambahkan label, field, dan button yang dibutuhkan
    def homepage(self):
        for i in range(len(self.dict_hotel)):
            # Membuat frame untuk setiap hotel dengan border color dan ketebalan yang diinginkan
            hotel_frame = tk.Frame(self.frame, borderwidth=2, relief=tk.GROOVE, background="#ffffff", bd=3)

            # Menentukan kolom untuk frame (kiri atau kanan)
            column = i % 2
            hotel_frame.grid(row=i // 2, column=column, padx=10, pady=10, sticky="ew")

            # Menambahkan label-label ke dalam frame
            label1 = tk.Label(hotel_frame, text=f"Nama Hotel: {self.dict_hotel[f'hotel{i+1}'][2]}", font=('Helvetica', 12), background="#ffffff")
            label2 = tk.Label(hotel_frame, text=f"Jumlah Kamar Tersedia: {self.dict_hotel[f'hotel{i+1}'][0]}", font=('Helvetica', 12), background="#ffffff")
            label3 = tk.Label(hotel_frame, text=f"Harga per Kamar: {self.dict_hotel[f'hotel{i+1}'][1]}", font=('Helvetica', 12), background="#ffffff")

            # Dimasukkan ke dalam frame
            label1.grid(row=0, column=0, pady=5, sticky="w")
            label2.grid(row=1, column=0, pady=5, sticky="w")
            label3.grid(row=2, column=0, pady=5, sticky="w")

    # Fungsi yang dipanggil saat ukuran frame diubah
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
