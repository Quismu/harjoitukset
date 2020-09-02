salasana = "koira"
annettuSalasana = input("Anna salasana: ")
while annettuSalasana != salasana:
    print("Väärä salasana!")
    annettuSalasana = input("Anna salasana: ")

if annettuSalasana == salasana:
    print("Tervetuloa!")
