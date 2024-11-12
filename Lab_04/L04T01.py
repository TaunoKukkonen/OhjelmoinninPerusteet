#Tee ohjelma, joka kysyy käyttäjältä kuinka monta kokonaislukua luodaan.
#Lisää listaan luvut niin että alkion arvo on alkion indeksi kertaa 10. 
#Huomaa, että indeksit alkavat nollasta (0). Tulosta taulukon sisältö konsoliin.

num=int(input("Kuinka monta kokonaislukua luodaan? "))

for x in range(num):
    print(f"{x+1 }.luku: {x*10}")


