#Tee ohjelma, joka kysyy käyttäjän etunimen ja syntymävuoden.
# Tämän jälkeen ohjelma laskee montako vuotta käyttäjä on (syntymäpäivää ja -kuukautta ei tarvitse huomioida) 
# Tämän jälkeen ohjelma kertoo kuinka vanha käyttäjä on.

import datetime

year = datetime.date.today().year

fname=input("Anna etunimesi ")

byear=int(input("Anna syntymävuotesi "))

print(f"Hei {fname}, olet {year-byear} vuotta vanha")