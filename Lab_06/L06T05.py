#uuma (engl. inch) on Brittiläisessä imperiumissa ja USA:ssa käytetty pituusmitta. 
# Yksi tuuma on 2.54 senttimetriä. Tee funktio show_cm, joka näyttää parametrina annetun tuumamitan sentteinä seuraavassa muodossa 2 tuumaa on 5,08 cm.

def show_cm(inc):
    cm=inc*2.54
    
    print(f"{inc} tuumaa on {cm} cm")
    
show_cm(12)