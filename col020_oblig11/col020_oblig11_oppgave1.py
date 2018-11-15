class Successor:
    counter = 0
    def __init__(self, nLen, retry):
        self.nLen = nLen
        self.retry = retry
        #self.counter = 0
    def get_next(self):
        if self.retry:
            if self.counter == self.nLen:
                self.counter=0
            print(self.counter)
            self.counter +=1
        else:
            if self.counter == self.nLen:
                print(None)
                return None
            print(self.counter)
            self.counter +=1
def main():
    while 1:
        try:
            size = int(input("Size: "))
            break
        except: 
            print('Only integers')
    do_loop = input("Loop [y/n]? ")
    if do_loop == 'y':
        loop = True
    else:
        loop = False
    asdf = Successor(size,loop)
    while 1: 
        asdf.get_next()
        quit = input('Enter q to quit:')
        if quit == 'q':
            break
 
if __name__ == '__main__':
    main()