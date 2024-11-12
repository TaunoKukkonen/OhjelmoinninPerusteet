#Tee ohjelma, joka kysyy käyttäjältä viikon kunkin päivän sademäärän.
# Sademäärä annetaan kokonaislukuna, jollei kyseisenä päivänä ole satanut käyttäjä antaa luvuksi 0.
# Laske ja näytä viikon kokonaissademäärä. 

numbase=0

for x in range(7):
    numbase +=int(input("anna sademäärä "))
    
print(f"sademäärä yhteensä {numbase}")
    