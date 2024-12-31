# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from fuzzy_control import fuzzy_control

def calculate():
    try:
        # Mendapatkan nilai input dari entry
        suhu_input = float(entry_suhu.get())
        kelembaban_input = float(entry_kelembaban.get())
        orang_input = float(entry_orang.get())
        
        # Validasi input
        if not (0 <= suhu_input <= 50):
            raise ValueError("Suhu harus antara 0°C dan 50°C.")
        if not (0 <= kelembaban_input <= 100):
            raise ValueError("Kelembaban harus antara 0% dan 100%.")
        if not (0 <= orang_input <= 30):
            raise ValueError("Jumlah orang harus antara 0 dan 30.")
        
        # Memanggil fungsi fuzzy_control
        out_suhu, kecepatan = fuzzy_control(suhu_input, kelembaban_input, orang_input)
        
        # Menampilkan hasil
        label_out_suhu.config(text=f"Suhu AC (Out Suhu): {out_suhu:.2f}°C")
        label_kecepatan.config(text=f"Kecepatan Angin (Kipas): {kecepatan:.2f}")
        
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Membuat jendela utama
root = tk.Tk()
root.title("Sistem Pengontrol Suhu AC Fuzzy")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Mengatur grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))
style.configure("TEntry", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10))

# Label dan Entry untuk Suhu
label_suhu = ttk.Label(root, text="Suhu (°C):")
label_suhu.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

entry_suhu = ttk.Entry(root)
entry_suhu.grid(column=1, row=0, sticky=tk.EW, padx=10, pady=10)

# Label dan Entry untuk Kelembaban
label_kelembaban = ttk.Label(root, text="Kelembaban (%):")
label_kelembaban.grid(column=0, row=1, sticky=tk.W, padx=10, pady=10)

entry_kelembaban = ttk.Entry(root)
entry_kelembaban.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=10)

# Label dan Entry untuk Jumlah Orang
label_orang = ttk.Label(root, text="Jumlah Orang:")
label_orang.grid(column=0, row=2, sticky=tk.W, padx=10, pady=10)

entry_orang = ttk.Entry(root)
entry_orang.grid(column=1, row=2, sticky=tk.EW, padx=10, pady=10)

# Tombol Hitung
button_calculate = ttk.Button(root, text="Hitung", command=calculate)
button_calculate.grid(column=0, row=3, columnspan=2, pady=20)

# Label Output Suhu AC
label_out_suhu = ttk.Label(root, text="Suhu AC (Out Suhu): -- °C", font=("Helvetica", 12, "bold"))
label_out_suhu.grid(column=0, row=4, columnspan=2, pady=10)

# Label Output Kecepatan Angin
label_kecepatan = ttk.Label(root, text="Kecepatan Angin (Kipas): --", font=("Helvetica", 12, "bold"))
label_kecepatan.grid(column=0, row=5, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()