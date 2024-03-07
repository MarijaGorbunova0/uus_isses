from modul import *
kasutajad = []
paroolid = []
polzovateli = []
while True:
    try:
        menu = int(input(" registreerimine - 1\n autoriseerimine - 2\n unustanud parooli taastamine - 3\n "))
        if menu == 1:
            nimi = input("registreerimine: kirjutage oma nimi")
            parool = input("registreerimine: kirjutage parool")
            zaregistr = registr(nimi, parool, kasutajad, paroolid)
            print("koik kasutajad", kasutajad)
        elif menu == 2:
            autoris(kasutajad, paroolid, polzovateli)
            if len(polzovateli) == 2:
                while True:
                    menu2 = int(input("nime või parooli muutmine - 1\n lõpetamine - 2\n "))
                    if menu2 == 1:
                        uus_parool_nimi(polzovateli, kasutajad, paroolid)
                    elif menu2 == 2:
                        polzovateli.clear()
                        print("olete oma kontolt välja logitud")
                        break
                    else:
                        print("vale andmetuup")
        elif menu == 3:
            email = input("kirjuta oma emaili")
            unustanudPR(paroolid, kasutajad)
        else:
            print("vale andmetüüp")
    except ValueError:
        print("kirjutage ainult numbrit")











