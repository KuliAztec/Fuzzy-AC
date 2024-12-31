# fuzzy_control.py

import numpy as np

# ---------------------------------------
# Fungsi Keanggotaan: Segitiga dan Trapesium
# ---------------------------------------

def triangular(x, a, b, c):
    """
    Fungsi keanggotaan segitiga.
    """
    return np.maximum(np.minimum((x - a) / (b - a + 1e-6), (c - x) / (c - b + 1e-6)), 0)

def trapezoidal(x, a, b, c, d):
    """
    Fungsi keanggotaan trapesium.
    """
    return np.maximum(np.minimum(np.minimum((x - a) / (b - a + 1e-6), 1), (d - x) / (d - c + 1e-6)), 0)

# ---------------------------------------
# Definisi Fungsi Keanggotaan untuk Input dan Output
# ---------------------------------------

# Fungsi Keanggotaan untuk Suhu
suhu_mf = {
    'sangat_rendah': lambda x: trapezoidal(x, 0, 0, 13, 18),
    'rendah': lambda x: triangular(x, 13, 18, 23),
    'sedang': lambda x: triangular(x, 18, 23, 28),
    'tinggi': lambda x: triangular(x, 23, 28, 33),
    'sangat_tinggi': lambda x: trapezoidal(x, 28, 33, 50, 50)
}

# Fungsi Keanggotaan untuk Kelembaban
kelembaban_mf = {
    'sangat_rendah': lambda x: trapezoidal(x, 0, 0, 30, 40),
    'rendah': lambda x: triangular(x, 30, 40, 50),
    'sedang': lambda x: triangular(x, 40, 50, 60),
    'tinggi': lambda x: triangular(x, 50, 60, 70),
    'sangat_tinggi': lambda x: trapezoidal(x, 60, 70, 100, 105)
}

# Fungsi Keanggotaan untuk Jumlah Orang
orang_mf = {
    'sedikit': lambda x: trapezoidal(x, 0, 0, 5, 10),
    'sedang': lambda x: triangular(x, 5, 10, 15),
    'banyak': lambda x: trapezoidal(x, 10, 15, 30, 35) 
}

# Fungsi Keanggotaan untuk Kecepatan Angin (Output)
kecepatan_mf = {
    'lambat': lambda x: trapezoidal(x, 1513, 1513, 1717, 1717),  # [1513, 1717]
    'sedang': lambda x: trapezoidal(x, 1717, 1717, 1921, 1921),  # [1717, 1921]
    'cepat': lambda x: trapezoidal(x, 1921, 1921, 2125, 2125)   # [1921, 2125]
}

# Fungsi Keanggotaan untuk Out Suhu (Output)
out_suhu_mf = {
    'tinggi': lambda x: trapezoidal(x, 25, 25, 30, 35),    
    'sedang': lambda x: trapezoidal(x, 20, 20, 25, 30)     
}

# ---------------------------------------
# Definisi Aturan Fuzzy
# ---------------------------------------

# Aturan untuk Out Suhu berdasarkan Suhu dan Jumlah Orang
rules_out_suhu = [
    # Suhu sangat rendah
    {'suhu': 'sangat_rendah', 'orang': 'sedikit', 'out_suhu': 'tinggi'},
    {'suhu': 'sangat_rendah', 'orang': 'sedang', 'out_suhu': 'tinggi'},
    {'suhu': 'sangat_rendah', 'orang': 'banyak', 'out_suhu': 'tinggi'},
    # Suhu rendah
    {'suhu': 'rendah', 'orang': 'sedikit', 'out_suhu': 'tinggi'},
    {'suhu': 'rendah', 'orang': 'sedang', 'out_suhu': 'tinggi'},
    {'suhu': 'rendah', 'orang': 'banyak', 'out_suhu': 'tinggi'},
    # Suhu sedang
    {'suhu': 'sedang', 'orang': 'sedikit', 'out_suhu': 'sedang'},
    {'suhu': 'sedang', 'orang': 'sedang', 'out_suhu': 'sedang'},
    {'suhu': 'sedang', 'orang': 'banyak', 'out_suhu': 'sedang'},
    # Suhu tinggi
    {'suhu': 'tinggi', 'orang': 'sedikit', 'out_suhu': 'sedang'},
    {'suhu': 'tinggi', 'orang': 'sedang', 'out_suhu': 'sedang'},
    {'suhu': 'tinggi', 'orang': 'banyak', 'out_suhu': 'sedang'},
    # Suhu sangat tinggi
    {'suhu': 'sangat_tinggi', 'orang': 'sedikit', 'out_suhu': 'sedang'},
    {'suhu': 'sangat_tinggi', 'orang': 'sedang', 'out_suhu': 'sedang'},
    {'suhu': 'sangat_tinggi', 'orang': 'banyak', 'out_suhu': 'sedang'},
]

# Aturan untuk Kecepatan Angin berdasarkan Suhu dan Kelembaban
rules_kecepatan = [
    # Suhu sangat rendah
    {'suhu': 'sangat_rendah', 'kelembaban': 'sangat_rendah', 'kecepatan': 'lambat'},
    {'suhu': 'sangat_rendah', 'kelembaban': 'rendah', 'kecepatan': 'lambat'},
    {'suhu': 'sangat_rendah', 'kelembaban': 'sedang', 'kecepatan': 'lambat'},
    {'suhu': 'sangat_rendah', 'kelembaban': 'tinggi', 'kecepatan': 'cukup'},
    {'suhu': 'sangat_rendah', 'kelembaban': 'sangat_tinggi', 'kecepatan': 'lambat'},
    # Suhu rendah
    {'suhu': 'rendah', 'kelembaban': 'sangat_rendah', 'kecepatan': 'lambat'},
    {'suhu': 'rendah', 'kelembaban': 'rendah', 'kecepatan': 'lambat'},
    {'suhu': 'rendah', 'kelembaban': 'sedang', 'kecepatan': 'cukup'},
    {'suhu': 'rendah', 'kelembaban': 'tinggi', 'kecepatan': 'cukup'},
    {'suhu': 'rendah', 'kelembaban': 'sangat_tinggi', 'kecepatan': 'cukup'},
    # Suhu sedang
    {'suhu': 'sedang', 'kelembaban': 'sangat_rendah', 'kecepatan': 'lambat'},
    {'suhu': 'sedang', 'kelembaban': 'rendah', 'kecepatan': 'cukup'},
    {'suhu': 'sedang', 'kelembaban': 'sedang', 'kecepatan': 'cukup'},
    {'suhu': 'sedang', 'kelembaban': 'tinggi', 'kecepatan': 'cepat'},
    {'suhu': 'sedang', 'kelembaban': 'sangat_tinggi', 'kecepatan': 'cepat'},
    # Suhu tinggi
    {'suhu': 'tinggi', 'kelembaban': 'sangat_rendah', 'kecepatan': 'cukup'},
    {'suhu': 'tinggi', 'kelembaban': 'rendah', 'kecepatan': 'cukup'},
    {'suhu': 'tinggi', 'kelembaban': 'sedang', 'kecepatan': 'cepat'},
    {'suhu': 'tinggi', 'kelembaban': 'tinggi', 'kecepatan': 'cepat'},
    {'suhu': 'tinggi', 'kelembaban': 'sangat_tinggi', 'kecepatan': 'cepat'},
    # Suhu sangat tinggi
    {'suhu': 'sangat_tinggi', 'kelembaban': 'sangat_rendah', 'kecepatan': 'cukup'},
    {'suhu': 'sangat_tinggi', 'kelembaban': 'rendah', 'kecepatan': 'cukup'},
    {'suhu': 'sangat_tinggi', 'kelembaban': 'sedang', 'kecepatan': 'cepat'},
    {'suhu': 'sangat_tinggi', 'kelembaban': 'tinggi', 'kecepatan': 'cepat'},
    {'suhu': 'sangat_tinggi', 'kelembaban': 'sangat_tinggi', 'kecepatan': 'cepat'},
]

# ---------------------------------------
# Fungsi Fuzzifikasi
# ---------------------------------------

def fuzzify(input_value, membership_functions):
    """
    Menghitung derajat keanggotaan untuk setiap kategori.
    """
    memberships = {}
    for key, func in membership_functions.items():
        memberships[key] = func(input_value)
    return memberships

# ---------------------------------------
# Fungsi Inferensi dengan Metode Tsukamoto
# ---------------------------------------

def infer_tsukamoto_out_suhu(rules, suhu_input, orang_input):
    """
    Inferensi untuk Out Suhu menggunakan Metode Tsukamoto dengan Weighted Average.
    """
    # Definisi fungsi output untuk Out Suhu
    out_suhu_funcs = {
        'tinggi': lambda x: 25 + 5 * x,    # y = 25 + 5 * firing_strength
        'sedang': lambda x: 20 + 5 * x     # y = 20 + 5 * firing_strength
    }
    
    # Fuzzification
    suhu_memberships = fuzzify(suhu_input, suhu_mf)
    orang_memberships = fuzzify(orang_input, orang_mf)
    
    # Debug: Tampilkan derajat keanggotaan
    print("Fuzzifikasi Out Suhu:")
    print(f"Suhu Memberships: {suhu_memberships}")
    print(f"Orang Memberships: {orang_memberships}")
    
    # Inferensi dengan Weighted Average
    numerator = 0
    denominator = 0
    
    for rule in rules:
        # Mendapatkan derajat keanggotaan untuk antecedents
        mu_suhu = suhu_memberships.get(rule['suhu'], 0)
        mu_orang = orang_memberships.get(rule['orang'], 0)
        
        # Operator AND (min) untuk menggabungkan derajat keanggotaan
        firing_strength = min(mu_suhu, mu_orang)
        
        # Debug: Tampilkan aturan dan firing strength
        print(f"Rule: IF Suhu is {rule['suhu']} AND Orang is {rule['orang']} THEN Out Suhu is {rule['out_suhu']}")
        print(f"  Firing Strength: {firing_strength}")
        
        if firing_strength > 0:
            # Hitung output menggunakan fungsi output
            out_suhu_func = out_suhu_funcs.get(rule['out_suhu'])
            if out_suhu_func:
                out_suhu_value = out_suhu_func(firing_strength)
                numerator += out_suhu_value * firing_strength
                denominator += firing_strength
                # Debug: Tampilkan nilai output dari aturan
                print(f"  Out Suhu Value: {out_suhu_value}")
    
    # Defuzzifikasi: Weighted Average
    if denominator != 0:
        out_suhu = numerator / denominator
        print(f"Defuzzifikasi Out Suhu: {out_suhu}")
    else:
        out_suhu = 0  # Nilai default jika tidak ada aturan yang aktif
        print("Defuzzifikasi Out Suhu: 0 (Default)")
    
    return out_suhu

def infer_tsukamoto_kecepatan(rules, suhu_input, kelembaban_input):
    """
    Inferensi untuk Kecepatan Angin menggunakan Metode Tsukamoto dengan Weighted Average.
    """
    # Definisi fungsi output untuk Kecepatan Angin
    kecepatan_funcs = {
        'lambat': lambda x: 1513 + (1717 - 1513) * x,     # y = 1513 + 204 * x
        'sedang': lambda x: 1717 + (1921 - 1717) * x,     # y = 1717 + 204 * x
        'cepat': lambda x: 1921 + (2125 - 1921) * x      # y = 1921 + 204 * x
    }
    
    # Fuzzification
    suhu_memberships = fuzzify(suhu_input, suhu_mf)
    kelembaban_memberships = fuzzify(kelembaban_input, kelembaban_mf)
    
    # Debug: Tampilkan derajat keanggotaan
    print("\nFuzzifikasi Kecepatan Angin:")
    print(f"Suhu Memberships: {suhu_memberships}")
    print(f"Kelembaban Memberships: {kelembaban_memberships}")
    
    # Inferensi dengan Weighted Average
    numerator = 0
    denominator = 0
    
    for rule in rules:
        # Mendapatkan derajat keanggotaan untuk antecedents
        mu_suhu = suhu_memberships.get(rule['suhu'], 0)
        mu_kelembaban = kelembaban_memberships.get(rule['kelembaban'], 0)
        
        # Operator AND (min) untuk menggabungkan derajat keanggotaan
        firing_strength = min(mu_suhu, mu_kelembaban)
        
        # Debug: Tampilkan aturan dan firing strength
        print(f"Rule: IF Suhu is {rule['suhu']} AND Kelembaban is {rule['kelembaban']} THEN Kecepatan Angin is {rule['kecepatan']}")
        print(f"  Firing Strength: {firing_strength}")
        
        if firing_strength > 0:
            # Hitung output menggunakan fungsi output
            kecepatan_func = kecepatan_funcs.get(rule['kecepatan'])
            if kecepatan_func:
                kecepatan_value = kecepatan_func(firing_strength)
                numerator += kecepatan_value * firing_strength
                denominator += firing_strength
                # Debug: Tampilkan nilai output dari aturan
                print(f"  Kecepatan Angin Value: {kecepatan_value}")
    
    # Defuzzifikasi: Weighted Average
    if denominator != 0:
        kecepatan = numerator / denominator
        print(f"Defuzzifikasi Kecepatan Angin: {kecepatan}")
    else:
        kecepatan = 0  # Nilai default jika tidak ada aturan yang aktif
        print("Defuzzifikasi Kecepatan Angin: 0 (Default)")
    
    return kecepatan


# ---------------------------------------
# Fungsi Kontrol Fuzzy
# ---------------------------------------

def fuzzy_control(suhu_input, kelembaban_input, orang_input):
    """
    Fungsi utama untuk menjalankan kontrol fuzzy.
    Mengembalikan (out_suhu, kecepatan_angin)
    """
    # Inferensi untuk Out Suhu
    out_suhu = infer_tsukamoto_out_suhu(rules_out_suhu, suhu_input, orang_input)
    
    # Inferensi untuk Kecepatan Angin
    kecepatan = infer_tsukamoto_kecepatan(rules_kecepatan, suhu_input, kelembaban_input)
    
    return out_suhu, kecepatan