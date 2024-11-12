#Tee ohjelma joka näyttää onko annettu vuosi karkausvuosi. Vuosiluku kysytään käyttäjältä. 
# Algoritmi: 4:llä jaolliset on, paitsi täydet vuosisadat. Kuitenkin 400:lla jaolliset vuosisadat ovat karkausvuosia. 
# Esim. 1991 -> ei, 1992 -> on, 1900 -> ei, 2000 -> on

userinput=int(input("Insert year: "))
if (userinput % 4==0) and (str(userinput)[-2:]!="00"):
    print(f"{userinput} is a leap year")
elif str(userinput)[-2:]=="00" and (int(userinput) % 400==0):   
     print(f"{userinput} is a leap year")
else:
     print(f"{userinput} in not a leap year")