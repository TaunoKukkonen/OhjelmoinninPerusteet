#Tee ohjelma, joka kysyy käyttäjän etunimen. 
# Tämän jälkeen ohjelma laskee ja näyttää montako kirjainta etunimessä on.
# Ohjelma toistaa käyttäjän etunimen kirjainta niin monta kertaa kun etunimessä on kirjaimia.


fname=input("Etunimesi ")

fletter= fname[0]

namelength=len(fname)

print(fletter*namelength)