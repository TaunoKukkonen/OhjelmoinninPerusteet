#Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. Lisää luokalle str metodi.
#Luokan str metodi toimii kuten on alla esitetty. Luo kaksi Human-luokan oliota seuraavilla tiedoilla: 
# Nimi: Adam, ikä: 19
# Nimi: Eva, ikä: 18 

class human:
    name= ""
    age= ""
    def __str__(self):
        return(f"nimi {self.name}, ikä: {self.age}")
    def __init__(self,name="" ,age="" ):
        self.name = name
        self.age = age
    
    
    
human1=human("Adam", 19)


human2=human("Eva",18)

print(human1)
print(human2)
