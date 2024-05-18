
from datetime import datetime


# Osztályok Létrehozása

class Szoba:
    def __init__(self, szobasz, ar):
        self.szobasz = szobasz
        self.ar = ar


class EgyagyasSzoba(Szoba):
    def __init__(self, szobasz, bed):
        super().__init__(szobasz, 50000)
        self.bed = bed


class KetagyasSzoba(Szoba):
    def __init__(self, szobasz, extra):
        super().__init__(szobasz, 65000)
        self.extra = extra


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglal_ok = []

    # Foglalások Kezelése

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobasz, datum):
        for foglal in self.foglal_ok:
            if foglal.szoba.szobasz == szobasz and foglal.datum == datum:
                print("\nA szoba már foglalt ezen a napon. \nVálasszon másik szobát vagy másik dátumot!")
                return
        for szoba in self.szobak:
            if szoba.szobasz == szobasz:
                self.foglal_ok.append(Foglalas(szoba, datum))
                print("Sikeres foglalás!")
                return szoba.ar
        print("\nA megadott szobaszám nem létezik.")

    def lmond(self, szobasz, datum):
        for foglal in self.foglal_ok:
            if foglal.szoba.szobsz == szobasz and foglal.datum == datum:
                self.foglal_ok.remove(foglal)
                return True
        return False

    def list_foglal_ok(self):
        for foglal in self.foglal_ok:
            print(f"Szoba: {foglal.szoba.szobasz}, Időpont: {foglal.datum}")


# Feltöltés: Szalloda létrehozása
hotel = Szalloda("Hotel Paradise")

# Feltöltés: Szobák hozzáadása
hotel.add_szoba(EgyagyasSzoba("101", "Összetolt ágy"))
hotel.add_szoba(EgyagyasSzoba("102", "Francia ágy"))
hotel.add_szoba(KetagyasSzoba("201", "TV"))

# Feltöltés: Foglalások hozzáadása
hotel.foglal("101", datetime(2024, 6, 12))
hotel.foglal("102", datetime(2024, 6, 20))
hotel.foglal("201", datetime(2024, 6, 25))
hotel.foglal("101", datetime(2024, 7, 10))
hotel.foglal("102", datetime(2024, 7, 18))

# Felhasználói interfész
while True:

    print("\nVálasszon műveletet:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Szobák listázása")
    print("5. Kilépés")
    case = input("Művelet kiválasztása (1/2/3/4/5): ")

    if case == "1":
        szobasz = input("\nAdd meg a foglalandó szoba számát: ")
        datum = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN, jelenleg csak egy napra lehetséges a foglalás): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("\nHibás dátum! A foglalás csak jövőbeni időpontra lehetséges.")
            else:
                ar = hotel.foglal(szobasz, datum)
                if ar:
                    print(f"A foglalás sikeres! Az ár: {ar} Ft")
                else:
                    print("\nHibás szobaszám!")
        except ValueError:
            print("\nHibás dátum formátum!")
    elif case == "2":
        szobasz = input("\nAdd meg a lemondandó foglalás szoba számát: ")
        datum = input("Add meg a lemondandó foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            siker = hotel.lmond(szobasz, datum)
            if siker:
                print("\nA foglalás sikeresen lemondva.")
            else:
                print("\nNincs ilyen foglalás.")
        except ValueError:
            print("\nHibás dátum formátum!")
    elif case == "3":
        hotel.list_foglal_ok()
    elif case == "4":
        print("Szobák száma:")
        print(len(hotel.szobak))
        print("Egyágyas szobák:")
        for szoba in hotel.szobak:
            if isinstance(szoba, EgyagyasSzoba):
                print(f"Szobaszám: {szoba.szobasz}, Ár: {szoba.ar} Ft, (Fürdő: {szoba.bed})")
        print("\nKétágyas szobák:")
        for szoba in hotel.szobak:
            if isinstance(szoba, KetagyasSzoba):
                print(f"Szobaszám: {szoba.szobasz}, Ár: {szoba.ar} Ft, (Extra: {szoba.extra})")
    elif case == "5":
        break
    else:
        print("\nHibás választás!")