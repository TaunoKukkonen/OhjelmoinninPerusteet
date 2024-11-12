

#käyttöön tulevat listat
grams=[]
gramsint=[]
type=[]
prep=[]
score=[]
scoreint=[]
#laskuri jolla selvitän mitä kahvintekotapaa käytetään eniten
def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
    return(itm)


#kysytään käyttäjältä kuinka monta grammaa ovat kahvia käyttäneet. kerrotaan kuinka paljon he ovat kahvia käyttäneet kokonaan
def gramfunct():
    try:
        consumedgrams=int(input("How many grams did you use?: "))
    except ValueError:
        print("give the amount in numbers")
        gramfunct()
        
    filename1="coffeegrams.txt"
    file=open(filename1,"a")
    file.write(str(consumedgrams)+" \n")
    file.close()
        
    file=open(filename1, "r")
    readfile=file.readlines()
    for x in readfile:
        grams.append(x.replace("\n", ""))
    
    for y in grams:
        gramsint.append(int(y))
        
    Sum=sum(gramsint)

    print(f"olet kuluttanut yhteensä {Sum}g kahvia")
    file.close
    

#kysytään minkä lajista kahvia käyttäjä on käyttänyt ja kerrotaan kuink amonta kertaa he ovat sitä juoneet
def typefunkt():
    coffeetype=input("Was the cofee arabica, robusta or something else?: ")
    if coffeetype=="arabica" or coffeetype=="robusta" or coffeetype=="something else":
        filename2="coffeetype.txt"
        file=open(filename2,"a")
        file.write(coffeetype+" \n")
        file.close()
    else:
        print("awnser only arabica, robusta or something else ")
        typefunkt()
    file=open(filename2, "r")
    
    readfile=file.readlines()
    for x in readfile:
        type.append(x.replace("\n", ""))
    arabica=type.count("arabica ")
    robusta=type.count("robusta ")
    sometingelse=type.count("something else ")
    print(f"You have drunk arabica {arabica} times, robusta {robusta} times and something else {sometingelse} times")
    file.close
        
#kysytään kahvinteko tapaa ja kerrotaan mikä niistä on ollut kaikista suosituin
def prepfunckt():
    coffeepreperation=input("How did you make the coffee?: ")
    filename3="coffeepreperation.txt"
    file=open(filename3,"a")
    file.write(coffeepreperation+" \n")
    file.close()
    file=open(filename3, "r")
    
    readfile=file.readlines()
    for x in readfile:
        prep.append(x.replace("\n", ""))
    print(f"{most_frequent(prep)} is your most used preparation method")
    file.close

#annetaan kahville pistemäärä ja kerrotaan kaikkien kahvien keskiverto pisteet
def scorefunct():
    try:
        coffeescore=int(input("on a scale on 1-5 how good was the coffee?: "))
    except ValueError:
        print("rate the coffee with numbers betweeen 1-5 ")
        scorefunct()
        
    filename4="coffeescore.txt"
    file=open(filename4,"a")
    file.write(str(coffeescore)+" \n")
    file.close()
    
    file=open(filename4, "r")
    readfile=file.readlines()
    for x in readfile:
        score.append(x.replace("\n", ""))
        
    for y in score:
        scoreint.append(int(y))
        
        Sum=sum(scoreint)
        Len=len(scoreint)

    print(f"Your coffees average score in {round(Sum/Len,1)} ja olet juonut {Len} kuppia kahvia")
    file.close

            

            
gramfunct()
typefunkt()
prepfunckt()
scorefunct()
