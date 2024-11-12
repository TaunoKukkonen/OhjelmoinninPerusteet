#Tee ohjelma, joka arpoo lottorivejä ja tallentaa ne tekstitiedostoon 'lotto.txt'. 
# Arvottu rivi sisältää seitsemän (7) numeroa väliltä 1-40. Käyttäjältä kysytään montako riviä arvotaan. 
# Varmista arpoessasi riviä, että sama numero ei esiinny kahta kertaa.

import random
result=[]
result=[]

def lotto():
    
      for x in range(7):
        number2=random.randint(1,40)
     
        while number2 in result:
             number2=random.randint(1,40)
        
        result.append(number2)
        
lotto()
strlist=str(result)
file1="lottorivi.txt"
file=open(file1,"w")
file.write(strlist)        
file.close()