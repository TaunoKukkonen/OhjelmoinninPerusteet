# Lataa oheinen tiedosto names.txt omalle koneellesi. Lisää tiedostoon oma nimesi viimeiseksi. Tee ohjelma, joka lukee tiedoston nimet ja ilmoittaa:
# a) montako nimeä tiedostossa on b) mikä nimistä on pisin
# Käytä poikkeustenkäsittelyä.
count=0
fnames={}

try:
    filename="names.txt"
    file=open(filename,"r")
    result=file.readlines()
    longest=max(result, key=len)
    numlines=len(result)
except :
    print("runtime error ocurred")


print(f"nimiä löytyi {numlines}")
print(f"pisin nimi on {longest}")

