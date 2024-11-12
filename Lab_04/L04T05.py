#Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen.
# Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia. 
# Tämän jälkeen tulosta käyttäjän sukunimi käänteisessä
# järjestyksessä. Siis esimerkiksi jos käyttäjä antaa etunimekseen 'Kirsi' ja sukunimeksi 'Kernell' suoritus olisi: 

fname=input("Anna etunimesi ")
lname=input("Anna sukunimesi ")
fnamelen=len(fname)
fletter=fname[0]

reverselname=lname[::-1]

print(f"{fletter*fnamelen} {reverselname}")
