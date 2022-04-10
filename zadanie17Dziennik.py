from datetime import datetime

oceny = {
    "Paweł": [3],
    "Kamil": [4],
    "Wiesiek": [5],
    "Mariola": [6,4]
}

def dodanie_ocen(slownik):
    chcesz_dodac = input("Chcesz dodać oceny? ")
    if chcesz_dodac.lower() == "tak":
        liczba_wpisow = int(input("Ilu osobom chcesz dodać oceny? "))
        for i in range(0,liczba_wpisow):
            imie = input("Podaj imie: ")
            ocena = list(input("Podaj ocene: "))
            ocena = [int(x) for x in ocena]
            if imie in slownik.keys():
                slownik[imie] += [int(x) for x in ocena]
            else:
                dodanie = {imie : ocena}
            slownik.update(dodanie)
    else:
        print("Ok")
    return slownik

def zapis(slownik):
    zapis_pliku_zapytanie = input("Czy chcesz zapisać oceny w pliku? ")
    if zapis_pliku_zapytanie.lower() == "tak":
        nazwa_pliku = input("Podaj nazwe pliku: ")
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(f"C:\\Users\\kubam\\desktop\\{nazwa_pliku}.txt" , "x") as plik_wyjsciowy:
            plik_wyjsciowy.write("Imię\t\tOcena\n")
            for key in slownik:
                plik_wyjsciowy.write(f"{key}\t{str(slownik[key])[1:-1]}\n")
            plik_wyjsciowy.write(f"Ostatnia modyfikacja pliku miała miejsce {date}\nSkrypt został utworzony przez JM")
    else:
        print("Ok")
            
def srednia(slownik):
    suma = 0
    n = 0
    for key in slownik:
        suma += sum(slownik[key])
        n += len(slownik[key])  
    return suma/n
            
def podglad(nazwa):
    podglad_pliku_zapytanie = input("Czy chcesz przejrzeć zapisany plik? ")
    if podglad_pliku_zapytanie.lower() == "tak":
        with open(f"C:\\Users\\kubam\\desktop\\{nazwa}.txt", "r") as podglad:
            print(podglad.read())
    else:
        print("Ok")

def zakonczenie():
    input("Kliknij zeby zakonczyc dzialanie skryptu")
    print("Dzialanie skryptu zostało zakończone")
    exit()

dodanie_ocen(oceny)
zapis(oceny)
podglad("ocenki")
print(f"Srednia ocen = {srednia(oceny)}")
zakonczenie()