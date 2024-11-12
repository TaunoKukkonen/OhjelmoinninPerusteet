#Tee ohjelma joka kysyy käyttäjältä kurssien arvosanoja (arvosana on kokonaisuluku 0,1,2,3,4 tai 5) ja tallentaa ne listaan.
# Käyttäjä voi syöttää niin monta kurssiarvosanaa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä.
# Näytä lopuksi montako arvosanaa käyttäjä antoi ja arvosanojen keskiarvo.

gradelist=[]

while True:
    userinput=input("Anna arvosana ")
    if userinput=="":
        break
    grade=int(userinput)
    gradelist.append(grade)
    
print(f"annettja arvosanoja {len(gradelist)}")
print(f"{sum(gradelist)/len(gradelist)}")