import matplotlib.pyplot as plt
import numpy as np

# 1. Dane
kanaly = np.array([801.88, 918.6, 1094.96, 1147.07, 1264.32, 1385.09])
energia_mev = np.array([3.5, 4, 4.76, 5, 5.5, 6])

# 2. Obliczenia dopasowania
a, b = np.polyfit(kanaly, energia_mev, 1)

# A. Linia ciągła do rysowania trendu (gładka)
x_fit_line = np.linspace(min(kanaly), max(kanaly), 100)
y_fit_line = a * x_fit_line + b

# B. Wartości z modelu w punktach pomiarowych (do obliczenia reszt)
y_model = a * kanaly + b

# C. Obliczenie reszt: (Wartość zmierzona) - (Wartość z modelu)
reszty = energia_mev - y_model

# # 3. Tworzenie wykresu z dwoma panelami (Subplots)
# # sharex=True: wspólna oś X
# # height_ratios=[3, 1]: górny wykres jest 3x wyższy od dolnego
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, 
#                             gridspec_kw={'height_ratios': [3, 1]})

# # --- GÓRNY PANEL: Kalibracja ---
# ax1.plot(kanaly, energia_mev, 'o', color='blue', markersize=6)
# ax1.plot(x_fit_line, y_fit_line, '-', color='red')#, label=f'Fit: E = {a:.5f}*Ch + {b:.4f}')
# ax1.set_ylabel('Energia (MeV)', fontsize=12)
# #ax1.set_title('Krzywa kalibracji i wykres reszt', fontsize=16)
# ax1.grid(True, linestyle='--', alpha=0.7)
# #ax1.legend()

# --- DOLNY PANEL: Reszty ---
plt.plot(kanaly, reszty, 's', color='green', markersize=6) # 's' = square markers
plt.axhline(0, color='black', linewidth=1.5) # Linia zerowa
plt.ylabel('Reszty (MeV)', fontsize=12)
plt.xlabel('Środkowy kanał', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Opcjonalne: przybliżenie wykresu reszt, by lepiej widzieć błędy
# ax2.set_ylim(-0.05, 0.05) 

plt.tight_layout() # Automatyczne dopasowanie odstępów
plt.savefig("reszty.pdf")