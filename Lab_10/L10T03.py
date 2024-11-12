#tee luokka account, jolla on ominaisuus saldo sekä metodit nostoa varten withdraw(money) ja tilille panoa varten add(money). 
# Tilille voi lisätä rahaa, ja tililtä voi nostaa rahaa, mutta vain sen verran kun tilillä on saldoa. 
# Tilin saldo ei voi olla negatiivinen, ja huom tarkistus täytyy tehdä luokan metodissa!

#Tee luokasta olio-muuttuja, johon alkusaldoksi lisäät aluksi on 2000€. Tulosta pankkitilin saldo konsoliin.
# Kysy konsolissa kuinka monta euroa lisätään saldoon. Lisää eurot saldoon ja näytä saldo konsolissa.
# Nosta sen jälkeen tililtä 1500€ ja näytä saldo. Koeta sen jälkeen nostaa tililtä uudestaan 1500€

class account:
    def __init__(self):
        self.saldo=2000
        self.money=0
        print("Bank account created.")
        print(f"account balance {self.saldo}€")
    
    
        
        
    def whithdraw(self):
        withdraw=int(input("How many euros will be withdrawn? "))
        if self.saldo-withdraw<0:
            print(F"Sorry, you have only {self.saldo}€, the withdraw cannot be done.")
        else:
            self.saldo-=withdraw
            print(f"account balance: {self.saldo}€")
        
        
        
    def add(self):
        add=int(input("How many euros will be added?  "))
        self.saldo+=add
        print(f"account balance: {self.saldo}€")
         
tili1=account()
tili1.add()
tili1.whithdraw()
tili1.whithdraw()