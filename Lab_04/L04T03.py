#Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja.
# Lukuja kysytään siihen saakka kunnes käyttäjä antaa tyhjän syötteen. Laske kuinka monta lukua käyttäjä antoi, laske myös annettujen lukujen summa. 
# Näytä annettujen lukujen lukumäärä ja summa käyttäjälle. 
amount=0
total=0
while True:
    try:
        userinput=input("Anna luku: ")
        num = int(userinput)
        total+=num
        amount=amount+1
    except ValueError:
        break
                
print(f"Annettuja lukuja: {amount}")
print(f"Lukujen summa: {total}")
