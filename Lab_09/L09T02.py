#Jatkoa edelliseen. Tee ohjelma, joka lukee edellisessä tehtävässä luodusta tiedostosta nimet ja näyttää ne konsolilla. 
# Tämän jälkeen ohjelma lajittelee nimet aakkosjärjestykseen ja näyttää ne konsolilla aakkosjärjestyksessä.
lnames=[]
filename="Last_names.txt"
file=open(filename,"r")
result= file.read()
splittedlnames=result.split()
lnames=splittedlnames
lnames_sorted=sorted(lnames)
print(lnames_sorted)
file.close()