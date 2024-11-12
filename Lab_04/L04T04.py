#Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen. Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia.
# Tämän jälkeen tulosta käyttäjän sukunimi käänteisessä järjestyksessä.
# Siis esimerkiksi jos käyttäjä antaa etunimekseen 'Kirsi' ja sukunimeksi 'Kernell' suoritus olisi: 

def numfunction():  
   num1=int(input("Anna luku 1-10 väliltä "))
   num2=0
   while True:
        if num1>num2 and num1<11:
         num2+=1
         print(f"luvun {num2} neliö on {num2*num2}")
         if num1==num2:
            break
        else:
           numfunction()  

numfunction()   
        



    
    
