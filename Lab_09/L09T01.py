#Tee ohjelma, joka kysyy käyttäjältä henkilöiden sukunimiä ja kirjoittaa käyttäjän antamat nimet tiedostoon.
# Nimiä kysytään niin kauan kunnes käyttäjä antaa tyhjän syötteen.
# Huomioi mahdolliset poikkeukset, joita tiedoston käsittely voi aiheuttaa.


lnames=[]
while True:
    userinput=input("Anna henkilöiden sukunimiä ")
    if userinput=="":
        break
    elif lnames=="":
        lnames=userinput
    else:
        lnames+=[userinput]
        

file1="Last_names.txt"
file=open(file1,"w")
for name in lnames:
    file.write(name+"\n")
file.close()
