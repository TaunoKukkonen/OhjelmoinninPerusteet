#Tee funktio get_cost(), jolle viedään 3 parametria. 
# Funktio laskee ja palauttaa automatkan polttoaineen hinnan. 
# Ensimmäinen parametri on ajetut kilometrit, toinen parametri on keskikulutus 100 km kohti ja kolmas parametri on polttoaineen litrahinta.
# Funktio palauttaa kustannuksen merkkijonona kahden desimaalin (eli sentin tarkkuudella) seuraavassa muodossa 14.10 €

def get_cost(drivendistance,avgconsumption,fuelcost):

    
    print(f"{round(drivendistance*avgconsumption/100*fuelcost,2)}€")
    
get_cost(220,6.9,1.88)
    