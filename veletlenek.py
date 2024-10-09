import random


def veletlenSzam():
    return random.randint(1, 100)  # 1 és 100 közötti véletlen szám


def parosSzamNégyzet(szam):
    if szam % 2 == 0:
        return szam ** 2
    else:
        return None


def egyAlap():
    szam1 = veletlenSzam()
    print(f"A véletlen szám: {szam1}")

    if szam1 % 2 == 0:
        négyzet = parosSzamNégyzet(szam1)
        print(f"Páros! A négyzete: {négyzet}")
    else:
        print("Páratlan")



def veletlenSzam():
    return random.randint(1, 12)  # 1 és 12 közötti véletlen szám

def honapNev(sorszam):
    honapok = [
        "Január", "Február", "Március", "Április", "Május", "Június",
        "Július", "Augusztus", "Szeptember", "Október", "November", "December"
    ]
    return honapok[sorszam - 1]

def egyAlap():
    szam1 = veletlenSzam()
    print(f"A véletlen szám: {szam1}")
    print(f"A hónap neve: {honapNev(szam1)}")

def beolvasSzam():
    while True:
        try:
            szam = int(input("Kérlek, adj meg egy egész számot (1-12 között): "))
            if 1 <= szam <= 12:
                return szam
            else:
                print("Hiba: Kérlek, egy számot adj meg 1 és 12 között!")
        except ValueError:
            print("Hiba: Kérlek, egy egész számot adj meg!")

def egyAlapEllenorzes():
    szam1 = beolvasSzam()
    print(f"A megadott szám: {szam1}")
    print(f"A hónap neve: {honapNev(szam1)}")


def szogTipusa(szam):
    if 0 < szam < 90:
        return "hegyesszög"
    elif szam == 90:
        return "derékszög"
    elif 90 < szam < 180:
        return "tompaszög"
    elif szam == 180:
        return "egyenes szög"
    elif 180 < szam < 360:
        return "tompaszög"  # A 180 és 360 közötti szögek tompaszögek
    elif szam == 360:
        return "fullszög"
    else:
        return None  # Ez soha nem érkezik ide, ha 0-360 között van

def beolvasSzam():
    while True:
        try:
            szam = float(input("Kérlek, adj meg egy valós számot (0-360 között): "))
            if 0 <= szam <= 360:
                return szam
            else:
                print("Hiba: Kérlek, egy számot adj meg 0 és 360 között!")
        except ValueError:
            print("Hiba: Kérlek, egy valós számot adj meg!")

def egyAlap():
    szam = beolvasSzam()
    print(f"A megadott szög: {szam} fok")
    tipusa = szogTipusa(szam)
    if tipusa:
        print(f"A szög típusa: {tipusa}")
    else:
        print("Hiba: Érvénytelen szög!")