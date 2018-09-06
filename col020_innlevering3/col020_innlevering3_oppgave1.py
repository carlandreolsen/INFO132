from random import randrange

modus = 2
# én variabel: helltallsvariabel modus med verdi 2
spor = randrange(modus)
# modus :: int = 2; spor (int) har verdi 0 eller 1
if spor:
    # siden spor >= 1 utføres nå det som ligger indentert under if statementet.
    svar = input("Skriv et tall mindre enn 10:\n")
    # nå har variabelen svar blitt bundet til en inputverdi med string type.
    try:
        # spor er 1 (int) og svar er fortsatt en string.
        svar = float(svar)
        # nå har svar blitt castet til en float type, om den var et rasjonalt tall med "." som desimalseparator. 
        if 0 <= svar and svar < 10:
            print("Ok!")
        else:
            print("Nei!")
            # her printes "Ok!" eller "Nei!" i forhold til hva brukerinpu var. Om tallet var 0 til og med 9 vil "Ok!" bli printet.            
        # Om spor ble 1 og svar var et tall er programmet ferdig her. 
    except:
        # Om svar ikke var et rasjonalt tall som input blir det under skrevet ut og programmet avsluttes.
        print(svar, " er ikke et tall.")
else:
    # siden spor ikke alltid blir != 0 havnet vi her.
    modus = spor * modus
    # spor vil i dette tilfellet alltid være 0. da blir modus også 0 her.
