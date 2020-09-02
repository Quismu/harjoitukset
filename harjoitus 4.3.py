salasana = "koira"
yritykset = 3

annettuSalasana = input("Anna salasana: ")
if annettuSalasana == salasana:
    print("Tervetuloa!")

if annettuSalasana != salasana and yritykset >= 1:
    print("Väärä salasana!")
    yritykset -= 1
    print("Yrityksiä jäljellä:",yritykset)
    annettuSalasana = input("Anna salasana: ")
    if annettuSalasana == salasana:
        print("Tervetuloa!")
    if annettuSalasana != salasana and yritykset >= 1:
        print("Väärä salasana!")
        yritykset -= 1
        print("Yrityksiä jäljellä:",yritykset)
        annettuSalasana = input("Anna salasana: ")
        if annettuSalasana == salasana:
            print("Tervetuloa!")
        if annettuSalasana != salasana:
            print("Yrityksesi loppuivat.")
