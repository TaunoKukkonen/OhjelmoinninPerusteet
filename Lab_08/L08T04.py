#Toteuta ohjelma, johon voi tallentaa kymmenen eri auton tiedot. Kustakin autosta tiedetään rekisterinumero (esim ABC-123) ja autonmerkki (esim Skoda).
# Keksi itse erilaisia rekisterinumeroita ja automerkkejä. 
# Tallenna tiedot valitsemaasi Dictionary-kokoelmaan. 
# Käytä rekisterinumeroa avaimena.
# Tulosta sen jälkeen autot aakkosjärjestyksessä rekisterinumeron mukaan.
garage={}

for x in range(10):
    regnum=input("Anna auton rekisterinumero: ")
    brand=input("Anna auton merkki: ")
    
    garage[regnum]=brand
    
myKeys = list(garage.keys())
myKeys.sort()
sorted_dict = {i: garage[i] for i in myKeys}
 
print(sorted_dict)    

