def funksjon1(minListe, positiveTall=[]):
    for i in minListe:
        if i < 0:
            continue
        else:
            positiveTall.append(i)
    return sum(positiveTall)

def funksjon2(minListe,tallFremTilNull=[]):
    for i in minListe:
        if i == 0:
            break
        else:
            tallFremTilNull.append(i)
    return sum(tallFremTilNull)

def funksjon3(minListe, divTall=[], zeroCount = 0, hitCount = 0):
    for i in minListe:
        if i == 0:
            zeroCount+=1
            if zeroCount == 2:
                return hitCount
        if i < 0:
            hitCount+=1
            continue
        if i%2:
            hitCount+=1
            
def main():
    #minListe = [5,2,-4,2,-1,0,2,-2,3,0,7]
    minListe = [-4, -7, -3, 0, -5, 6, 0, 2, -1, 7, 0, -4, 6, 3]
    print(funksjon1(minListe))
    print(funksjon2(minListe))
    print(funksjon3(minListe))
    


if __name__ == '__main__':
    main()
