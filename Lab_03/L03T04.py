#Tee ohjelma jossa annetaan oppilaalle arvosana alla olevan taulukon mukaan. Kysy pistemäärä konsolissa ja tulosta arvosana.

point = int(input("Anna saadut pisteet "))

if point<=1:
    print("Arvosana 0")
elif point<=3:
    print("Arvosana 1")
elif point<=5:
    print("Arvosana 2")
elif point<=7:
    print("Arvosana 3")
elif point<=9:
    print("Arvosana 4")
elif point<=12:
    print("Arvosana 5")
