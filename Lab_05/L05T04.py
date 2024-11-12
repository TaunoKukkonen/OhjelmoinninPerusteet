#Tee funktio get_fuel(), jolle viedään 2 parametria. Funktio laskee ja palauttaa automatkaan kuluneen polttoaineen määrän.
# Ensimmäinen parametri on ajetut kilometrit, toinen parametri on keskikulutus 100 km kohti.
# Funktio palauttaa merkkijonona kulutuksen yhden desimaalin tarkkuudella seuraavassa muodossa 15.2 ltr. 


def get_fuel(drivendistance,avgconsumption):
    
   
    print(f"{round(drivendistance*avgconsumption/100,1)} ltr")
    
get_fuel(400,8)