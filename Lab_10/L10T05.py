#Tee ohjelma, jolla yrität kirjoittaa tekstitiedoston 'ayho.txt' (sisällön saat päättää itse) Windows-koneen kovalevyn C:n juureen (macOS/Linux/Unix-koneilla käyttäjän juurihakemistoon).
# Mitä tapahtui? Kaatuiko ohjelma virheeseen? Korjaa ohjelma niin, ettei se kaadu, eli lisää siihen tarvittava poikkeustenkäsittely. 

import os.path
os.chdir("C:\\")
try:
    letters=["Y","A","A","R"]
    filepath = os.path.join("c:\\")
    filename="ahoy.txt"
    file=open(filename,"w")
    for letter in letters:
        file.write(letter +"\n")
    file.close()
except:
    print("Ei ole lupaa luoda kansiota, kokeile ajaa järjestelmän valvojana")

