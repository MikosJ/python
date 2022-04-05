#monte carlo
import math
import random
import numpy as np
import matplotlib.pyplot as plt

"""Ilość trafień w okrągłą tarcze do ilości trafień w kwadratową tarczę
ma się jak pole koła do pola tarczy

Wyznaczyć wartość pi"""
print("Program wylicza wartość \u03C0 wykorzystując zależność, że liczba trafień w okrągłą tarcze o średnicy 2r do liczby trafień w tarcze kwadratową o boku 2r ma się jak pole koła do pola tarczy.")
r = float(input("Podaj długość promienia R\n"))
liczba = int(input("Podaj ile wartości ma zostać wylosowane\n"))

x = random.choices(np.arange(-r,r,0.01),k = liczba)
y = random.choices(np.arange(-r,r,0.01),k = liczba)
trafienia = 0

d = []
for a in range(0,liczba):
    d.append(math.sqrt(x[a]**2+y[a]**2))

for i in d:
    if i < r:
        trafienia += 1
pi = 4*trafienia/liczba

roznica = float(abs((math.pi - pi))/math.pi)*100
print(f'Na podstawie {liczba} wartości dla figur w przedziale r równym {r} oszacowano \u03C0 z tej zależności które wynosi: {pi}\nRzeczywista wartość \u03C0 = {math.pi}\nRóżnica wynosi {round(roznica,2)}%')


#wykorzystalem biblioteke matplotlib by zwizualizowac wynik
plt.plot(x,y,'.',alpha = 0.1,lw=3, color = '#29D004')
kolko = plt.Circle((0,0), r, color = '#64004D', fill = False)
fig = plt.gcf()
ax = fig.gca()
ax.add_patch(kolko)
plt.show()
