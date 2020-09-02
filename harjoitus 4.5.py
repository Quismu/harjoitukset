luku1 = int(input("Syötä ensimmäinen luku: "))
luku2 = int(input("Syötä toinen luku: "))
laskutoimitus = (input("Syötä laskutoimitus (+, -, *, /): "))

if(laskutoimitus == "+"): print(luku1,"+",luku2,"=",luku1+luku2)
if(laskutoimitus == "-"): print(luku1,"-",luku2,"=",luku1-luku2)
if(laskutoimitus == "*"): print(luku1,"*",luku2,"=",luku1*luku2)
if(laskutoimitus == "/"): print(luku1,"/",luku2,"=",luku1/luku2)
