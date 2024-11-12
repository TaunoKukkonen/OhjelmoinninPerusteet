# Mäkihypyssä käytetään viittä arvostelutuomaria. Jokainen antaa hypylle pisteitä yhdestä kahteenkymmeneen 1-20.
# Kirjoita ohjelma, joka kysyy arvostelupisteet yhdelle hypylle ja tulostaa tyylipisteiden summan siten, että summasta on vähennetty pois pienin ja suurin tyylipiste. 
points=0
point1=int(input("Anna pisteet "))
point2=int(input("Anna pisteet "))
point3=int(input("Anna pisteet "))
point4=int(input("Anna pisteet "))
point5=int(input("Anna pisteet "))
list1=[point1,point2,point3,point4,point5]


points=point1+point2+point3+point4+point5-max(list1)-min(list1)


    
print(points)
