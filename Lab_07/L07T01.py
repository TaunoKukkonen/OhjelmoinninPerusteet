#Tee luokka Pelikortti. Luokalla on kaksi ominaisuutta: maa ja arvo. 
# Maa on: pata, hertta, ruutu tai risti. Arvo on jokin luku 2-14. Luokan ei tarvitse kuitenkaan mitenkään tarkista että olion ominaisuudet ovat edellä mainitut.
# Luo viisi Pelikortti-oliota erilaisilla ominaisuuksilla.
# Näytä korttien tiedot esimerkiksi seuraavasti print(kortti1.maa , kortti1.arvo). 

class Pelikortti:
    maa: str()
    arvo: int(1-14)
    
kortti1=Pelikortti()
kortti1.maa= "pata"
kortti1.arvo= "2"


kortti2=Pelikortti()
kortti2.maa= "hertta"
kortti2.arvo= "5"


kortti3=Pelikortti()
kortti3.maa= "risti"
kortti3.arvo= "10"

kortti4=Pelikortti()
kortti4.maa= "ruutu"
kortti4.arvo= "3"

kortti5=Pelikortti()
kortti5.maa= "pata"
kortti5.arvo= "12"

print(kortti1.maa , kortti1.arvo)