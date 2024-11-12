#Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja ja tallentaa annetut luvut tiedostoon luvut.txt. 
# Ohjelma lopettaa lukujen kysymisen, kun käyttäjä antaa tyhjän syötteen. 
# Viimeiseksi ohjelma kirjoittaa tiedostoon montako lukua käyttäjä antoi seuraavasti: Syötetty 5 lukua.
# Tarkista lopuksi tiedoston sisältö tekstieditorilla.
numlist=[]
count=0
while True:
    try:
        userinput=str(input("Anna kokonaislukuja: "))
        if userinput=="":
            break
        elif numlist=="":
            numlist=userinput
            count+=1
        else:
            numlist.append(userinput)
            count+=1
    except:
        break
file1="luvut.txt"
file=open(file1,"w")
for num in numlist:
    file.write(num+"\n")
file.write(f"syötetty{count} lukua.")
file.close()
