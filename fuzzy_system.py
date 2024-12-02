import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
suhu = ctrl.Antecedent(np.arange(0, 50, 1), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0, 100, 1), 'kelembaban')
orang = ctrl.Antecedent(np.arange(0, 30, 1), 'orang')

# Define labels suhu & kelembaban
sangat_rendah = 'sangat_rendah'
rendah = 'rendah'
sedang = 'sedang'
tinggi = 'tinggi'
sangat_tinggi = 'sangat_tinggi'

# Define labels orang
sedikit = 'sedikit'
sedang = 'sedang'
banyak = 'banyak'


# Define membership functions for suhu
suhu[sangat_rendah] = fuzz.trapmf(suhu.universe, [0, 0, 13, 18])
suhu[rendah] = fuzz.trimf(suhu.universe, [13, 18, 23])
suhu[sedang] = fuzz.trimf(suhu.universe, [18, 23, 28])
suhu[tinggi] = fuzz.trimf(suhu.universe, [23, 28, 33])
suhu[sangat_tinggi] = fuzz.trapmf(suhu.universe, [28, 33, 50, 50])

# Define membership functions for kelembaban
kelembaban[sangat_rendah] = fuzz.trapmf(kelembaban.universe, [0, 0, 30, 40])
kelembaban[rendah] = fuzz.trimf(kelembaban.universe, [30, 40, 50])
kelembaban[sedang] = fuzz.trimf(kelembaban.universe, [40, 50, 60])
kelembaban[tinggi] = fuzz.trimf(kelembaban.universe, [50, 60, 70])
kelembaban[sangat_tinggi] = fuzz.trapmf(kelembaban.universe, [60, 70, 100, 100])

# Define membership functions for orang
orang[sedikit] = fuzz.trapmf(orang.universe, [0, 0, 5, 10])
orang[sedang] = fuzz.trimf(orang.universe, [5, 10, 15])
orang[banyak] = fuzz.trapmf(orang.universe, [10, 15, 30, 30])

# Define labels for kecepatan_angin
kecepatan_angin = ctrl.Consequent(np.arange(1500, 2500, 1), 'kecepatan_angin', 'lom')
lambat = 'lambat'
cukup = 'sedang'
cepat = 'cepat'

# Define membership functions for kecepatan_angin
kecepatan_angin[lambat] = fuzz.trimf(kecepatan_angin.universe, [1513, 1513, 1819])
kecepatan_angin[cukup] = fuzz.trimf(kecepatan_angin.universe, [1717, 1819, 1921])
kecepatan_angin[cepat] = fuzz.trimf(kecepatan_angin.universe, [1819, 2125, 2125])

#suhu keluaran
out_suhu =ctrl.Consequent(np.arange(0, 50, 1), 'out_suhu', 'lom')

# Define membership functions for suhu`keluar`
out_suhu[sangat_rendah] = fuzz.trapmf(suhu.universe, [13, 13, 15, 18])
out_suhu[rendah] = fuzz.trapmf(suhu.universe, [15, 18, 21, 23])
out_suhu[sedang] = fuzz.trapmf(suhu.universe, [20, 23, 26, 28])
out_suhu[tinggi] = fuzz.trapmf(suhu.universe, [25, 28, 30, 33])
out_suhu[sangat_tinggi] = fuzz.trapmf(suhu.universe, [28, 30, 33, 33])

# buat speed
rule1 = ctrl.Rule(suhu[sangat_rendah] & kelembaban[sangat_rendah], kecepatan_angin[lambat])
rule2 = ctrl.Rule(suhu[sangat_rendah] & kelembaban[rendah], kecepatan_angin[lambat])
rule3 = ctrl.Rule(suhu[sangat_rendah] & kelembaban[sedang], kecepatan_angin[lambat])
rule4 = ctrl.Rule(suhu[sangat_rendah] & kelembaban[tinggi], kecepatan_angin[cukup])
rule5 = ctrl.Rule(suhu[sangat_rendah] & kelembaban[sangat_tinggi], kecepatan_angin[lambat])

rule6 = ctrl.Rule(suhu[rendah] & kelembaban[sangat_rendah], kecepatan_angin[lambat])
rule7 = ctrl.Rule(suhu[rendah] & kelembaban[rendah], kecepatan_angin[lambat])
rule8 = ctrl.Rule(suhu[rendah] & kelembaban[sedang], kecepatan_angin[cukup])
rule9 = ctrl.Rule(suhu[rendah] & kelembaban[sangat_tinggi], kecepatan_angin[cukup])
rule10 = ctrl.Rule(suhu[rendah] & kelembaban[tinggi], kecepatan_angin[cukup])

rule11 = ctrl.Rule(suhu[sedang] & kelembaban[sangat_rendah], kecepatan_angin[lambat])
rule12 = ctrl.Rule(suhu[sedang] & kelembaban[rendah], kecepatan_angin[cukup])
rule13 = ctrl.Rule(suhu[sedang] & kelembaban[sedang], kecepatan_angin[cukup])
rule14 = ctrl.Rule(suhu[sedang] & kelembaban[tinggi], kecepatan_angin[cepat])
rule15 = ctrl.Rule(suhu[sedang] & kelembaban[sangat_tinggi], kecepatan_angin[cepat])

rule16 = ctrl.Rule(suhu[tinggi] & kelembaban[sangat_rendah], kecepatan_angin[cukup])
rule17 = ctrl.Rule(suhu[tinggi] & kelembaban[rendah], kecepatan_angin[cukup])
rule18 = ctrl.Rule(suhu[tinggi] & kelembaban[sedang], kecepatan_angin[cepat])
rule19 = ctrl.Rule(suhu[tinggi] & kelembaban[tinggi], kecepatan_angin[cepat])
rule20 = ctrl.Rule(suhu[tinggi] & kelembaban[sangat_tinggi], kecepatan_angin[cepat])

rule21 = ctrl.Rule(suhu[sangat_tinggi] & kelembaban[sangat_rendah], kecepatan_angin[cukup])
rule22 = ctrl.Rule(suhu[sangat_tinggi] & kelembaban[rendah], kecepatan_angin[cukup])
rule23 = ctrl.Rule(suhu[sangat_tinggi] & kelembaban[sedang], kecepatan_angin[cepat])
rule24 = ctrl.Rule(suhu[sangat_tinggi] & kelembaban[tinggi], kecepatan_angin[cepat])
rule25 = ctrl.Rule(suhu[sangat_tinggi] & kelembaban[sangat_tinggi], kecepatan_angin[cepat])


# buat temp
ruleb1 = ctrl.Rule(suhu[sangat_rendah] & orang[sedikit], out_suhu[tinggi])
ruleb2 = ctrl.Rule(suhu[sangat_rendah] & orang[sedang], out_suhu[tinggi])
ruleb3 = ctrl.Rule(suhu[sangat_rendah] & orang[banyak], out_suhu[tinggi])

ruleb4 = ctrl.Rule(suhu[rendah] & orang[sedikit], out_suhu[tinggi])
ruleb5 = ctrl.Rule(suhu[rendah] & orang[sedang], out_suhu[tinggi])
ruleb6 = ctrl.Rule(suhu[rendah] & orang[banyak], out_suhu[tinggi])

ruleb7 = ctrl.Rule(suhu[sedang] & orang[sedikit], out_suhu[sedang])
ruleb8 = ctrl.Rule(suhu[sedang] & orang[sedang], out_suhu[sedang])
ruleb9 = ctrl.Rule(suhu[sedang] & orang[banyak], out_suhu[sedang])

ruleb10 = ctrl.Rule(suhu[tinggi] & orang[sedikit], out_suhu[sedang])
ruleb11 = ctrl.Rule(suhu[tinggi] & orang[sedang], out_suhu[sedang])
ruleb12 = ctrl.Rule(suhu[tinggi] & orang[banyak], out_suhu[sedang])

ruleb13 = ctrl.Rule(suhu[sangat_tinggi] & orang[sedikit], out_suhu[sedang])
ruleb14 = ctrl.Rule(suhu[sangat_tinggi] & orang[sedang], out_suhu[sedang])
ruleb15 = ctrl.Rule(suhu[sangat_tinggi] & orang[banyak], out_suhu[sedang])


# Create the control system with the rules
get_speed = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25])
simu_speed = ctrl.ControlSystemSimulation(get_speed)

# Create the control system with the rules
get_temp = ctrl.ControlSystem([ruleb1, ruleb2, ruleb3, ruleb4, ruleb5, ruleb6, ruleb7, ruleb8, ruleb9, ruleb10, ruleb11, ruleb12, ruleb13, ruleb14, ruleb15])
simu_temp = ctrl.ControlSystemSimulation(get_temp)

# Input values
in_suhu = 0
in_kelembaban = 100
in_orang = 30

#Matplotlib
#suhu.view()
#kelembaban.view()
#orang.view()
#kecepatan_angin.view()
#out_suhu.view() 
#input('Enter Jadi ilang')

# Assign the input values to the fuzzy variables
simu_speed.input['suhu'] = in_suhu
simu_speed.input['kelembaban'] = in_kelembaban

# Assign the input values to the fuzzy variables
simu_temp.input['suhu'] = in_suhu  # Add this line
simu_temp.input['orang'] = in_orang

# Perform the computation
simu_speed.compute()
simu_temp.compute()

# Output the result
#print("Kecepatan angin: ", simu_speed.output['kecepatan_angin'])
# kecepatan_angin.view(sim=simu_speed)  # Show output fuzzy set with computed result

#print("Suhu: ", simu_temp.output['out_suhu'])
# out_suhu.view(sim=simu_temp)  # Show output fuzzy set with computed result

# Debug
#input('Enter Jadi ilang')