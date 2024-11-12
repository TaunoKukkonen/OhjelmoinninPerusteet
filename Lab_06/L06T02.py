#Tee funktiot: celToFah() ja fahToCel()
#ahToCel() muuttaa fahrenheitit celsiuksiksi. Muutettu astearvo palautetaan yhden desimaalin tarkkuudella. 
# yTestaa kumpikin funktio kutsumalla sitä käyttäjän antamilla luvuilla. 

def celTofah(cel):
    fah= cel*1.8+32
    return(round(fah,1))
    
def fahTocel(fare):
    cels=(fare - 32) *0.5556
    return(round(cels,1))
    
print(celTofah(10))

print(fahTocel(38.0))