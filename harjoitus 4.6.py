vuosi = int(input("Anna vuosi: "))
if vuosi % 100 == 0:
    if vuosi % 400 == 0: print("Vuosi",vuosi,"on karkausvuosi.")
    if vuosi % 400 != 0: print("Vuosi",vuosi,"ei ole karkausvuosi.")
if vuosi % 100 != 0:
    if vuosi % 4 == 0: print("Vuosi",vuosi,"on karkausvuosi.")
    if vuosi % 4 != 0: print("Vuosi",vuosi,"ei ole karkausvuosi.")
