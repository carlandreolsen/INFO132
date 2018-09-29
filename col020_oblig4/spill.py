from hangman import correct_guess

def main():
    løsning = "hangman"
    forsøk = "efhg"
    neste = ""
    resultat = None
    neste = input("Skriv inn en bokstav: ")
    resultat = correct_guess(løsning, forsøk, neste)
    if resultat==None:
        print("Har du prøvd denne bokstaven før eller har du skrevet inn mer enn 1?")
    elif resultat == True:
        print("Riktig.")
    else:
        print("Feil.")
        
if __name__ == '__main__':
    main()
