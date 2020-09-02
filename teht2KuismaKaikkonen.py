import random

tavoiteltavaLuku = random.randint(1,100) # luo satunnaisluku, jota tavoitellaan

print("Voit lopettaa pelin kirjoittamalla: lopeta") # ohje
annettuLuku = int(input("Veikkaa lukua 1-100: ")) # ensimmäinen käyttäjän input

yritykset = 1

while annettuLuku != tavoiteltavaLuku: # kun veikkaaminen on vielä kesken

    if int(annettuLuku) < tavoiteltavaLuku: # jos käyttäjä veikkaa liian pientä lukua
        print("")
        annettuLuku = int(input("Veikkaa suurempaa lukua: "))
    if int(annettuLuku) > tavoiteltavaLuku: # jos käyttäjä veikkaa liian suurta lukua
        print("")
        annettuLuku = int(input("Veikkaa pienempää lukua: "))

    yritykset += 1 # kasvattaa yrityksien määrää yhdellä

if annettuLuku == tavoiteltavaLuku: # kun käyttäjä veikkaa oikein
    print("")
    print("Hyvä, onnistuit!")
    print("Yritykset:",yritykset)
      
