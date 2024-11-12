#Tee funktio showtime(), joka muuttaa parametrinä saadun sekuntiarvon merkkijonoksi muotoon tunnit:minuutit:sekunnit. Funktio palauttaa seuraavasti:
#- jos tunteja alle kymmenen muodossa 02:46:40 - jos tunteja yli kymmenen muodossa 12:46:40
#Sama myös minuuteissa.

def showtime(sec):
    sec = sec %(24 * 3600 )
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)

print(showtime(10000))