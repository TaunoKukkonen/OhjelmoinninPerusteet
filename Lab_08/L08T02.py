#Toteuta ohjelma, joka kysyy käyttäjältä autojen rekisterinumeroita (siis esim 'ABC-123' jne) ja tallentaa ne listaan.
# Käyttäjä voi syöttää niin monta rekisterinumeroa kuin haluaa, 
# syöttäminen lopetetaan tyhjällä syötteellä. Näytä syötetyt rekisterinumero aakkosjärjestyksessä.

registratuonnumbers=[]

while True:
    userinput=input("Anna rekisterinumero: ")
    if userinput=="":
        break
    registratuonnumbers.append(userinput)
    
registratuonnumbers.sort()
print(registratuonnumbers)
    
    
