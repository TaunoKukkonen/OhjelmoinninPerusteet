#Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen.
# Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna. 

amount=0
names=""
while True:
    userinput=input("Anna oppilaan nimi: ")
    if userinput=="":
        break
    student=userinput
    if names=="":
        names=student
    else:
        names  =names +", "+  student
        
    nameslist=names
    amount=amount+1
                
print(f"Oppilaita: {amount}")
print(nameslist)
