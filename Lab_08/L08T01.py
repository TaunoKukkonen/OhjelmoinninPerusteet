#Tee ohjelma, joka kysyy käyttäjältä kymmenen kaverin nimen. Ohjelma näyttää ensin kaverit annetussa järjestyksessä.
# Seuraavaksi ohjelma näyttää kaverit käännetyssä järjestyksessä, eli viimeiseksi annetun ensimmäisenä jne.



namelist=[]

for x in range (10):    
    userinput=input("Anna kaverin nimi ")
    namelist.append(userinput)
        
    
print(namelist)
namelist.reverse()
print(namelist.reverse())
    