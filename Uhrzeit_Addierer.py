# Dieses Programm mit 3 Zahlen und zwar stunden, minuten und mit der Zahl welche dazu addiert werden muss. 
def uhrzeit_minuten_addieren(stunden, minuten, summand):
    # Mehr als 60 Minuten werden in Stunden umgerechnet
    while minuten+summand>=60:
        minuten=minuten-60
        stunden=stunden+1
    # Mehr als 24 Stunden werden in weniger umgerechnet, ganze Tage werden nicht gespeichert.
    while stunden>=24:
        stunden=stunden-24
    # Die Zeit wird ausgegeben.
    print(str(stunden) +":" + str(minuten+summand))

uhrzeit_minuten_addieren(17, 32, 8) # 17:32 + 8 Min = 17:40
uhrzeit_minuten_addieren(19, 7, 63) # 19:07 + 63 Min = 20:10
uhrzeit_minuten_addieren(16, 10, 1111) # 16:10 + 1111 Min = 10:41
