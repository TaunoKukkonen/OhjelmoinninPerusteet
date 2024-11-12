#Autotallissasi on kolme autoa. Tee luokka Car. Car-luokalla on kolme ominaisuutta: brand, model ja price.
# Luo Car-luokasta vähintään kolme erilaista auto-oliota. Aseta autojen ominaisuudet seuraavasti: 
# 1) brand="Skoda" model="Octavia" price=3000 2) brand="Audi" model="A4" price=4000 3) brand="Volvo" model="V70" price=5000

#Tulosta kaikkien autotallin kolmen auton ominaisuudet konsolille. Laske myös autojen yhteishinta, ja näytä se konsolilla:

class car:
   
    def __init__(self, brand="" ,model="",price=""):
        self.brand=brand
        self.model=model
        self.price=price
        
    def __str__(self):
        return(f"auto: {self.brand} {self.model} {self.price}")

car1=car("skoda","octavia", 3000)
car2=car("audi", "a4", 4000)
car3=car("volvo","v70", 5000)

print(car1)
print(car2)
print(car3)
print(car1.price+car2.price+car3.price)