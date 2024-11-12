#Tee ohjelma, joka kysyy käyttäjän etu- ja sukunimen. Tämän jälkeen ohjelman näyttää käyttäjän kokonimen isoilla kirjaimilla. 



fname=input("Anna etunimesi ")

lname=input("Anna sukunimesi ")

names= [fname, lname] #pitää olla pilkku fnamen ja lnamen välissä eikä +

fullname=" ".join(names) 

print(fullname.upper())