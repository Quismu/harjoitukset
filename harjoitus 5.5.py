print("Hei käyttäjä!")
print("")
luku = int(input("Anna positiivinen luku: "))
while luku <= 0:
    print("Ei, luvun pitää olla positiivinen!")
    print("")
    luku = int(input("Anna positiivinen luku: "))

if luku > 0:
    print("Hyvä, osasit!")

