#Tee luokka Cat. Tee Cat-luokalle kaksi ominaisuutta name ja color, sekä yksi metodi miau. Luo Cat-luokasta kaksi erilaista kissa-oliota seuraavilla tiedoilla:
# name: Kit, color: black
# name: Kat, color: white

class cat:
    name=""
    color=""
    
    
    def __init__(self, name="" ,color="",):
        self.name=name
        self.color=color
        
        
    def __str__(self):
        return(f"{self.name} says: Meoooooow! ")
        
cat1=cat("kit","white")
cat2=cat("kat","black")
print(cat1)
print(cat2)