table = "female\tIngelin\tAleksandersen\nmale\tJohnny\tDigre\nmale\tOsman\tBremseth\nfemale\tCathrine\tDagestad\nfemale\tTirill\tBakker"
 
def show_table():
    print(table)
 
def show_every_cell():
  tbl=table.split('\n')
  fulltbl=[]
  for i in tbl:
    fulltbl.append(i.split('\t'))
  for i in range(0,len(fulltbl)):
    for j in range(0,len(fulltbl[i])):
      print('Row:%i Col:%i Value:%s'%(i,j,fulltbl[i][j]))
 
def main():
    show_table()
    print('')
    show_every_cell()
   
if __name__ == "__main__":
    main()
