annettuLuku = int(input("Anna luku: "))

eksponentti = 2
kantaluku = 1
termit = kantaluku
luku = 0
while luku < annettuLuku:
    kantaluku += 1
    luku += kantaluku^eksponentti
    termit += 1
    print(luku)
print(termit)

    
    
