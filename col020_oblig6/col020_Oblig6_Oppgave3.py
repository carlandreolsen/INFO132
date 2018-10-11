def equilibrium():
  texttoparse = input('Give me your parathesis.')
  dybde=0
  for i in texttoparse:
    if i == '(':
      dybde+=1
    elif i == ')':
      dybde-=1
    else:
      return 'Invalid input...'
    if dybde <0:
      break
  if dybde == 0:
    return 'Uttrykket er balansert.'
  elif dybde > 0:
    return 'Uttrykket er ubalansert.'
  else:
    return None
  
def main():
  while 1:
    print(equilibrium())
if __name__ == '__main__':
  main()
