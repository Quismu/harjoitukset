import random

tavoiteltavaLuku = random.randint(1,100) # luo satunnaisluku, jota tavoitellaan

print("Luku pitää ilmoittaa kokonaislukuna.") # ohje
print()
annettuInput = input("Veikkaa lukua 1-100: ")
yritykset = 0

while True: # ikuinen loop
    if annettuInput.isdigit():
        if int(annettuInput) < tavoiteltavaLuku: # jos syötetty luku on liian pieni
            yritykset += 1
            annettuInput = input("Veikkaa suurempaa lukua: ")
        if int(annettuInput) > tavoiteltavaLuku: # jos syötetty luku on liian iso
            yritykset += 1
            annettuInput = input("Veikkaa pienempää lukua: ")
        if int(annettuInput) == tavoiteltavaLuku: # jos käyttäjä veikkaa oikein
            yritykset += 1
            print("")
            print("Hyvä, onnistuit!")
            print("Yritykset:",yritykset) # yritysten näyttäminen
            break # ohjelma "loppuu"
