import tkinter as tk
from tkinter import ttk, messagebox
# Import fuzzy logic system from original file
from fuzzy_system import simu_speed, simu_temp, kecepatan_angin, out_suhu

class FuzzyControlGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Kontrol Fuzzy")
        
        # Configure root window
        self.root.geometry("800x600")  # Adjust window size
        self.root.configure(padx=20, pady=20, bg="#f0f0f0")  # Add padding and background color
        
        # Configure grid weight
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create main frame with border
        main_frame = ttk.Frame(self.root, relief="solid", borderwidth=1, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Style configuration
        style = ttk.Style()
        style.configure('TLabelframe', borderwidth=2, relief="solid", padding="10")
        style.configure('TButton', padding=10, font=('Helvetica', 12, 'bold'))
        style.configure('TLabel', padding=5, font=('Helvetica', 10))
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)
        
        # Suhu input
        ttk.Label(input_frame, text="Suhu (0-50°C)").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.suhu_var = tk.StringVar(value="25")
        self.suhu_entry = ttk.Entry(input_frame, textvariable=self.suhu_var)
        self.suhu_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Kelembaban input
        ttk.Label(input_frame, text="Kelembaban (30-100%)").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.kelembaban_var = tk.StringVar(value="60")
        self.kelembaban_entry = ttk.Entry(input_frame, textvariable=self.kelembaban_var)
        self.kelembaban_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Jumlah orang input
        ttk.Label(input_frame, text="Jumlah Orang (0-30)").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.orang_var = tk.StringVar(value="10")
        self.orang_entry = ttk.Entry(input_frame, textvariable=self.orang_var)
        self.orang_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Calculate button in its own frame
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(button_frame, text="Hitung", command=self.calculate, style='TButton').pack()
        
        # Output frame
        output_frame = ttk.LabelFrame(main_frame, text="Hasil", padding="10")
        output_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        output_frame.grid_columnconfigure(1, weight=1)
        
        # Output labels with better formatting
        ttk.Label(output_frame, text="Kecepatan Angin:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.speed_result = ttk.Label(output_frame, text="-", font=('Helvetica', 14, 'bold'))
        self.speed_result.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(output_frame, text="Suhu Output:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.temp_result = ttk.Label(output_frame, text="-", font=('Helvetica', 14, 'bold'))
        self.temp_result.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    
    def calculate(self):
        try:
            # Get input values
            suhu = float(self.suhu_var.get())
            kelembaban = float(self.kelembaban_var.get())
            orang = float(self.orang_var.get())
            
            # Validate input ranges
            if not (0 <= suhu <= 50):
                raise ValueError("Suhu harus antara 0-50°C")
            if not (30 <= kelembaban <= 100):
                raise ValueError("Kelembaban harus antara 30-100%")
            if not (0 <= orang <= 30):
                raise ValueError("Jumlah orang harus antara 0-30")
            
            # Calculate speed
            simu_speed.input['suhu'] = suhu
            simu_speed.input['kelembaban'] = kelembaban
            simu_speed.compute()
            
            # Calculate temperature
            simu_temp.input['suhu'] = suhu
            simu_temp.input['orang'] = orang
            simu_temp.compute()
            
            # Update results
            self.speed_result.config(text=f"{simu_speed.output['kecepatan_angin']:.2f} rpm")
            self.temp_result.config(text=f"{simu_temp.output['out_suhu']:.2f}°C")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = FuzzyControlGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()