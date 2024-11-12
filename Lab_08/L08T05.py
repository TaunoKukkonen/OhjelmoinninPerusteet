#Tee funktio lotto(), joka arpoo lottorivin seitsemän (7) numeroa väliltä 1-40 ja palauttaa sen merkkijonona, luvut eroteltuna pilkuilla. Siis esimerkiksi näin: 1,3,5,10,20,33,39
#Käytä lukujen arpomiseen Pythonin valmista modulia random ja sen metodia randint, kts lisää: https://www.w3schools.com/python/gloss_python_random_number.asp

import random
result=[]

def lotto():
    
    #  number1=random.randint(1,40)  
    #  result.append(number1)
     for x in range(7):
        number2=random.randint(1,40)
     
        while number2 in result:
             number2=random.randint(1,40)
        
        result.append(number2)
        
        
    #  number3=random.randint(1,40)
    #  while number3 in result:
    #      number3=random.randint(1,40)
    #  result.append(number3)
    #  number4=random.randint(1,40)
    #  while number4 in result:
    #      number4=random.randint(1,40)
    #  result.append(number4)
    #  number5=random.randint(1,40)
    #  while number5 in result:
    #      number5=random.randint(1,40)
    #  result.append(number5)
    #  number6=random.randint(1,40)
    #  while number6 in result:
    #      number6=random.randint(1,40)
    #  result.append(number6)
    #  number7=random.randint(1,40)
    #  while number7 in result:
    #      number3=random.randint(1,40)
    #result.append(number7)
        
         
     print(result)
        
        
lotto()