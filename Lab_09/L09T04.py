#Lataa tämä tekstitiedosto nimet.txt koneellesi.
# Tiedostossa on henkilöitten nimiä. Sama nimi saattaa esiintyä monta kertaa. 
# Tee ohjelma, joka lukee em. 
# tekstitiedostosta nimet ja kertoo montako nimeä löytyy ja montako kertaa kukin nimi esiintyy. 
# Käytä Dictionary-kokoelmaa ratkaisussasi.
key=0
names={}
from collections import Counter

filename="nimet.txt"
file=open(filename,"r")
result=file.read()
split_names=result.split()

for nimi in split_names:
       key+=1
       names[key]=split_names[key-1]
       

        
print(names)
namecheck= Counter(names.values())
print(namecheck)