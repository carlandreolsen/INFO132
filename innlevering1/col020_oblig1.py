#variabelen n er lagret i primærlageret. 
#col020_oblig1.py er lagret i sekundærlageret.
#python er en interpreter.
#Erstatt verdi bundet til n for å skrive ut summen av de n første Fibonacci tallene
n = 1234
#Legger til et ekstra listelement, 0, på starten for å slippe å gjøre unntak for første iterasjon.
fibonacciListOfNumbers = [0,1]
for i in range(0,n-1):
    fibonacciListOfNumbers.append(fibonacciListOfNumbers[i]+fibonacciListOfNumbers[i+1])
#Fibonacci-rekken 1,1,2,3,5,8,13,21,34,...  
#print(x)
print(sum(fibonacciListOfNumbers[0:n+1]))
