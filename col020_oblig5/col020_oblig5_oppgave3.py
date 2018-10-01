def main():
    tall=0.0
    while 1:
        userInput = input("Skriv et tall eller avslutt:")
        if userInput=='avslutt':
            break
        try:
            tall = tall + float(userInput)
            print(tall)
        except:
            print("Du skrev hverken et tall eller 'avslutt'...")        
    print("Adjø!")

if __name__ == '__main__':    
    main()
