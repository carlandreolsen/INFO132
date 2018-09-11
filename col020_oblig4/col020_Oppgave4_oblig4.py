def fibonacci(n): #https://youtu.be/_tcW-j7KFgY?t=1m30s
    if n == 1:
        return 1
    else:
        return (n+fibonacci(n-1))
def main():
    tekst = input("Skriv inn et heltall")
    try:
        tallet = int(tekst)
        print(fibonacci(tallet))
    except:
        print("Prøv igjen. Du skal skrive inn et heltall.")
if __name__ == '__main__':
    main()
