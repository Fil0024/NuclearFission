import numpy as np
import matplotlib.pyplot as plt



# 1. Dane przykładowe
# Oś X: Środkowy kanał (centroid piku)
kanaly = [801.88, 918.6, 1094.96, 1147.07, 1264.32, 1385.09]

# Oś Y: Energia w MeV (np. odpowiadająca znanym izotopom)
energia_mev = [3.5, 4, 4.76, 5, 5.5, 6]

a, b = np.polyfit(kanaly, energia_mev, 1)

# Tworzenie teoretycznej linii na podstawie wyliczonych a i b
x_fit = np.linspace(min(kanaly), max(kanaly), 100) # 100 punktów od min do max kanału
y_fit = a * x_fit + b


#DOPASOWANIE
plt.figure(figsize=(10, 6))

# Rysujemy punkty pomiarowe (same kropki 'o')
plt.plot(kanaly, energia_mev, 'o', markersize=6, color='blue')

# Rysujemy linię dopasowania
# W etykiecie (label) formatujemy równanie, żeby pokazało się w legendzie
plt.plot(x_fit, y_fit, '-', color='red', linewidth=2)

#plt.title("Kalibracja energetyczna z dopasowaniem liniowym", fontsize=16)
plt.xlabel("Środkowy kanał", fontsize=12)
plt.ylabel("Energia (MeV)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 5. Wyświetlenie
plt.savefig("dopasowanie.pdf")



#PUNKTY
print(f"Równanie kalibracji: Energia = {a:.5f} * Kanal + {b:.5f}")

plt.figure(figsize=(10, 6))

# Rysujemy punkty pomiarowe (same kropki 'o')
plt.plot(kanaly, energia_mev, 'o', markersize=8, color='blue')

#plt.title("Kalibracja energetyczna z dopasowaniem liniowym", fontsize=16)
plt.xlabel("Środkowy kanał", fontsize=12)
plt.ylabel("Energia (MeV)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
#plt.legend(fontsize=12)

# 5. Wyświetlenie
plt.savefig("punkty.pdf")

# Wypisanie równania w konsoli dla pewności
print(f"Równanie kalibracji: Energia = {a:.5f} * Kanal + {b:.5f}")
