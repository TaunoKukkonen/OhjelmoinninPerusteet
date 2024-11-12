#Tee ohjelma, jossa kysytään käyttäjältä tämän syntymävuoden. Annetun syntymävuoden perusteella laske henkilön ikä. 
# Jotta ohjelmasi toimisi oikein myös tulevina vuosina, hae kuluva vuosi tietokoneen kellosta, eli käytä esim datetime.date.today()-metodia.
# Tee ohjelmaan funktio kerro3(age), joka iän perusteella palauttaa seuraavan tekstin:
#- jos ikä on alle 1 vuotta, palautetaan "baby"
#- jos ikä on alle 13 vuotta, palautetaan "child"
#- jos ikä on 13-19 vuotta, palautetaan "teen"
#- jos se on 20-65 vuotta, palautetaan "adult"
#- muussa tapauksessa palautetaan "senior". 

import datetime
year = datetime.date.today().year
userinput=int(input("Kerro syntymävuotesi: "))
age=year-userinput
if age<1:
    print("baby")
elif age<13:
    print("child")
elif age<19:
    print("teem")
elif age<65:
    print("adult")
else:
    print("senior")