#Tee ohjelma, joka kysyy käyttäjän kokonimen. Tämän jälkeen ohjelma erottaa annetusta merkkijonosta välilyönnin perusteella käyttäjän etu- ja sukunimen.
#Vinkki 1: Merkkijono muuttujasta nimi voi hakea välilyönnin paikan seuraavalla funktiolla.
#i = nimi.find(' ')
#Vinkki 2: Voit palauttaa merkkijonosta halutun osan käyttämällä slice-syntaksia. 
# Määritä aloitusindeksi ja loppuindeksi kaksoispisteellä erotettuina palauttaaksesi osan merkkijonosta. 


fname,lname=input("Anna koko nimesi ").split()
print("Etunimesi on "+ fname)
print("Sukunimesi on "+lname)