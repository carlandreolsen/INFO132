#Caecar cipher
alphabet = "abcdefghijklmnopqrstuvwxyzæøå ?"
def clean_text(inputForScrub):
  scrubbedInput = ''
  for i in inputForScrub:
    if i not in alphabet:
      scrubbedInput=scrubbedInput+'?'
    else:
      scrubbedInput=scrubbedInput+i
  return scrubbedInput
def symbol_add(symbol,key):
  startIndex = alphabet.find(symbol)
  if startIndex == -1:
    print('Not valid character.')
    return -1
  #Her blir modulo brukt for å starte fra 0 igjen når index blir høyere enn lengede på stringen alphabet.
  return alphabet[(startIndex+key)%len(alphabet)]
  
def cipher(data,key):
  cleanData=''
  chipherData=''
  for i in data:
    cleanData=cleanData+(clean_text(i))
  for i in cleanData:
    chipherData=chipherData+symbol_add(i,key)
  return chipherData
def main():
  print('Ctrl+C to stop cipher.')
  while 1:
    userText=input('Text for chiper.')
    while 1:
      try:      
        userKey=int(input('Write an integer index missplacement.'))
        break
      except:
        pass
    print(cipher(userText,userKey))
if __name__ == '__main__':
  main()
