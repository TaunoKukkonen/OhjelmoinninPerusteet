#Tee ohjelma, joka kysyy käyttäjältä viisi lukua. Laske annetuista luvuista yhteen ne luvut, 
# jotka ovat nollaa suurempia. Siis jos käyttäjä antaa nollan tai negatiivisen luvun sitä ei lisätä summaan.
# Tulosta summa konsoliin. Kokeile ohjelmaasi esim seuraavilla arvoilla: 1,2,3,4,5 ja -2,0,2,4,6. Mitä sait summaksi? 

num1 =int(input("Anna luku 1 "))
num2 =int(input("Anna luku 2 "))
num3 =int(input("Anna luku 3 "))
num4 =int(input("Anna luku 4 "))
num5 =int(input("Anna luku 5 "))
total=int()
if num1>0:
    total += num1
if num2>0:
    total += num2
if num3>0:
    total += num3
if num4>0:
    total += num4
if num4>0:
    total += num5
    
print(total)

