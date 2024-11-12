#Tee luokka Mobile. 
# Mobile-luokalla on kolme ominaisuutta: brand, model ja price.
# Lisää luokalle konstruktori init jolla voidaan oliota luodessa asettaa edellä mainitut ominaisuudet. Luo kaksi uutta Mobile-oliota seuraavalla koodilla:

class Mobile:
    brand=""
    model=""
    price=""
    
    
    def __init__(self, brand="" ,model="",price=""):
        self.brand=brand
        self.model=model
        self.price=price
        
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

print(f"{phone1.brand} {phone1.model} {phone1.price}€")
print(f"{phone2.brand} {phone2.model} {phone2.price}€")
