#Tee ohjelma, joka kysyy käyttäjältä kokonaisluvun. Annetun luvun perusteella ohjelma toimii seuraavasti:
# - jos luku on 10 tai 20, palauta teksti "Luku on 10 tai 20" - jos luku on 100 tai 200, palauta teksti "Luku on 100 tai 200" - 
# muuten palauta annettu luku tekstinä, siis esim "Luku on 1".

num1=int(input("Anna kokonaisluku "))

if num1 ==10 or num1==20:
    print("luku on 10 tai 20")
elif num1 ==100 or num1==200:
    print("luku on 100 tai 200")
else:
    print(f"luku on {num1}")