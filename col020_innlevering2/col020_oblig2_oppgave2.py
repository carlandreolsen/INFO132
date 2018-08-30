# Her importerer vi en funksjon. Vi komer tilbake til dette om et par uker.
# Behold denne linjen uendret i din besvarelse.
from random import randrange

# Dette programmet er et mynt og kron spill.

# input() funksjonen skriver ut en tekst og venter på at bruker skal skrive inn noe og trykke på enter.
# Dette blir da bundet til variabelen tippetTekst som en tekststreng.
tippetTekst = input("Tipp simulert terningkast 1 til 6... ")

# her blir tekststrengen lagret i tippetTekst gjort om til et heltall, om mulig, og blir bundet til en ny variabel kalt tippetTall.
tippetTall = int(tippetTekst)

# randarange genererer med input som under et tall fra 1 til 6. Tallet blir bundet til variabelen faktiskTall som et heltall.
faktiskTall = randrange(6)+1

# her blir det brukt en sammenligningsoperator for å sjekke om tippetTall er det samme som faktiskTall.
# om de er like vil det resultere i True, eller False om feil. Resultat vil bli bundet til variabelen tippet Riktig.
tippetRiktig = tippetTall == faktiskTall

print("Du tippet")
print(tippetTall)
print("Riktig tall var")
print(faktiskTall)
print("Hadde du rett?")
print(tippetRiktig)
