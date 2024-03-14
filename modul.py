import random
from operator import index
from kasutajad import kasutajad, paroolid, polzovateli
import smtplib, ssl
from email.message import EmailMessage
#1
def registr(nimi, parool, kasutajad:list, paroolid:list): #registrerimine
   if nimi in kasutajad:
       print("kirjutage uus nimi")
   else:
       kasutajad.append(nimi)
       paroolid.append(parool)
       kirjuta_failisse()
       print("Registreerimine õnnestus.")
       return kasutajad,paroolid
#2
def autoris(kasutajad: list, paroolid: list, polzovateli): #autoriseerimine
    nimi = input("Kirjutage oma nimi: ")
    if nimi in kasutajad:
        nimiIndeks = kasutajad.index(nimi)
        parool = input("Kirjutage parool: ")
        if parool == paroolid[nimiIndeks]:
            print("Kõik on hästi")
            polzovateli.append(nimi)
            polzovateli.append(parool)
            return kasutajad, paroolid
        else:
            print("Vale parool")
            return kasutajad, paroolid
    else:
         print("Sulle vaja registreerida")
         return kasutajad, paroolid
#3
def uus_parool_nimi(polzovateli, kasutajad: list, paroolid: list): #uue paroli registrerimine
    zamena = int(input("kirjutage mida te tahate vahetada parol - 1, nimi - 2"))
    if zamena == 2:
        uusNimi = input("kirjutage uus nimi ")
        polzovateli[0] = uusNimi
        kasutajad[0] = uusNimi
        print("teie nimi on edukalt muudetud!")
        return polzovateli
    elif zamena == 1:
        uusParol = input("kirjutage uus parool ")
        polzovateli[1] = uusParol
        paroolid[0] = uusParol
        print("teie parool on edukalt muudetud!")
        return polzovateli

#4
def unustanudPR(paroolid, kasutajad): #unustanud parooli
    nimi = input("kirjutage oma nimi")
    if nimi in kasutajad:
        kiri = int(input("te tahte vahetada parooli? kinnitada - 1\n parooli lähtestamise tühistamine – 2"))
        while True:
            if kiri == 1:
                smtp_server = "smtp.gmail.com"
                port = 587
                sender_email = input("kirjutage mail")
                while True:
                    if "@" not in sender_email:
                        print("siin ei oie @")
                    else:
                        password = input("Type your password(copied gmail) ")
                        #create a secure SSL conntex
                        context = ssl.create_default_context()
                        msg = EmailMessage()
                        msg.set_content = 324
                        msg["Subject"] = "324"
                        msg["From"] = sender_email
                        msg["To"] = sender_email
                        #"try to log to server and email
                        try:
                            server = smtplib.SMTP(smtp_server, port)
                            server.ehlo() #can be omitted
                            server.starttls(context = context)
                            server.ehlo()
                            server.login(sender_email, password)
                            #server.sendmail(sender_email, msg)
                            server.send_message(msg)
                        except Exception as Viga:
                            print(Viga)
                        finally:
                            server.quit()
                            sbros = int(input("kirjutage kood "))
                        while True:
                            if sbros == msg.set_content:
                                nimiIndeks = kasutajad.index(nimi)
                                uusParol = input("kirjutage uus parool ")
                                paroolid[nimiIndeks] = uusParol
                                kirjuta_failisse()
                                break
                            else:
                                print("vale kood")
                        break
                    break
                if kiri == 2:
                    print("te tühistasite parooli lähtestamise")
                    break
                else:
                    print("vale andmetüüp, provige veel üks kord")
        else:
            print("selle nimega kasutajat pole")

def kirjuta_failisse():
    with open("kasutajad.py", "w", encoding="utf-8") as f: #loome uus mutujat f
        f.write(f"kasutajad = {kasutajad}\n")
        f.write(f"paroolid = {paroolid}\n")
        f.write(f"polzovateli = {polzovateli}\n")