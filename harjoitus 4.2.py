password = "kissa"
inputPassword = input("Syötä salasana: ")
tries = 3;

if(inputPassword == password): print("Tervetuloa!")

if(inputPassword != password and tries == 3): {
    print("Väärä salasana!")
    print("Yrityksiä jäljellä 2")
    tries -= 1
    print("")
    inputPassword = input("Syötä salasana: ")
}

if(inputPassword != password and tries == 2): {
    print("Väärä salasana!")
    print("Yrityksiä jäljellä 1")
    tries -= 1
    print("")
    inputPassword = input("Syötä salasana: ")
}

if(inputPassword != password and tries == 1): {
    print("Väärä salasana!")
    print("Yritykset loppuivat")
}

