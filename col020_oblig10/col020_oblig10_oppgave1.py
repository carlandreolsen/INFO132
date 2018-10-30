def fileToList(filename):
    try:
        my_file = open(filename+'.csv', encoding="utf-8", mode='r')
    except:
        print("Could not find file with name '%s'"%filename)
        return 0
    my_file_content = my_file.read()
    my_file.close()
    my_file_content = my_file_content.split('\n')
    my_list =[]
    for i in my_file_content:
        my_list.append(i.split('\t'))
    return my_list

def printNameSexFriendsNear(agentid,peoplelist,friendslist,nearlist):
    print("Name: %s %s"%(peoplelist[agentid][1],peoplelist[agentid][2]))
    print("Sex: %s"%(peoplelist[agentid][0]))
    friendcount = 0
    for i in friendslist:
        if str(agentid) in i:
            friendcount +=1
    print('Friend counter: %i'%friendcount)
    nearcount = 0
    for i in nearlist:
        if str(agentid) in i:
            nearcount +=1
    print('People in area: %i'%nearcount)

def printFriendsandNear(agentid,peoplelist,friendslist,nearlist):
    for i in friendslist:
        if str(agentid) in i:
            if int(i[0]) == agentid:
                print("Friend Name: %s %s"%(peoplelist[int(i[1])][1],peoplelist[int(i[1])][2]))
            else:
                print("Friend Name: %s %s"%(peoplelist[int(i[0])][1],peoplelist[int(i[0])][2]))
    for i in nearlist:
        if str(agentid) in i:
            if i[0] == i[1]:
                pass 
            elif int(i[0]) == agentid:
                print("Nearby Person: %s %s"%(peoplelist[int(i[1])][1],peoplelist[int(i[1])][2]))
            else:
                print("Nearby Person: %s %s"%(peoplelist[int(i[0])][1],peoplelist[int(i[0])][2]))
def printNearbyFriends(agentid,friendslist,nearlist):
    stubbed_friendslist = []
    for i in range(0,len(friendslist)):
        if str(agentid) in friendslist[i]:
            if friendslist[i][0] == friendslist[i][1]:
                pass 
            elif int(friendslist[i][0]) == agentid:
                stubbed_friendslist.append(friendslist[i][1])
            else:
                stubbed_friendslist.append(friendslist[i][0])
    #print(stubbed_friendslist)
    nearfriendcounter=0
    for i in nearlist:
        if str(agentid) in i:
            for j in stubbed_friendslist:
                if j in i:
                    nearfriendcounter+=1
    print('Nearby Friends: %i'%nearfriendcounter)

def printNewFriendSuggestion(agentid,peoplelist,friendslist):
    for i in friendslist:
        if str(agentid) in i:
            if int(i[0]) == agentid:
                for j in friendslist:
                    if i[1] == j[0] and j[1] != str(agentid):
                        print('Suggested New Friend: %s %s'%(peoplelist[int(j[1])][1],peoplelist[int(j[1])][2]))
                        return 0
                    elif i[1] == j[1] and j[0] != str(agentid):
                        print('Suggested New Friend: %s %s '%(peoplelist[int(j[0])][1],peoplelist[int(j[0])][2]))
                        return 0
            else:
                for j in friendslist:
                    if i[0] == j[0] and j[0] != str(agentid):
                        print('Suggested New Friend: %s %s '%(peoplelist[int(j[1])][1],peoplelist[int(j[1])][2]))
                        return 0
                    elif i[0] == j[1] and j[1] != str(agentid):
                        print('Suggested New Friend: %s %s '%(peoplelist[int(j[0])][1],peoplelist[int(j[0])][2]))
                        return 0
    return 0

def printTwoNearbyPeopleNotFriends(agentid,peoplelist,friendslist,nearlist):
    stubbed_nearlist = []
    for i in range(0,len(nearlist)):
        if str(agentid) in nearlist[i]:
            if nearlist[i][0] == nearlist[i][1]:
                pass 
            elif int(nearlist[i][0]) == agentid:
                stubbed_nearlist.append(nearlist[i][1])
            else:
                stubbed_nearlist.append(nearlist[i][0])
    #print(stubbed_nearlist)
    candidates=[]
    matchcount=0
    for i in range(0,len(stubbed_nearlist)):
        for j in friendslist:
            if stubbed_nearlist[i] in j:
                for k in range(0,len(stubbed_nearlist)):
                    if j[1] != stubbed_nearlist[k]:
                        candidates.append(int(stubbed_nearlist[k])) 
                        matchcount+=1
                        if matchcount == 2:
                            #print(candidates)
                            print('Two nearby people that are not friends: %s %s & %s %s'%(peoplelist[candidates[0]][1],peoplelist[candidates[0]][2],peoplelist[candidates[1]][1],peoplelist[candidates[1]][2]))
                            return 1

def main():
    nodesfile = 'noder_25_3'
    edgesfile = 'kanter_25_3'
    colocationfile = 'naboer_25_3'
    peoplelist = fileToList(nodesfile) #Oppgave 1.1
    friendslist = fileToList(edgesfile) #Oppgave 1.1
    nearlist = fileToList(colocationfile) #Oppgave 1.1
    """
    for i in range(0,len(peoplelist)):
        print(peoplelist[i] +[i])
    print()
    print(friendslist)
    print()
    print(nearlist)
    
    for i in range(0,len(peoplelist)):

        agentid = i
    """
    while True:
        try:
            agentid = int(input("Skriv inn agent-ID: "))
        except:
            print('Kun heltall...')
            continue
        if agentid > 24:
            print('Agent-ID fra 0-24, det er bare 25 agenter...')
            continue
        printNameSexFriendsNear(agentid,peoplelist,friendslist,nearlist) #Oppgave 1.2
        print()
        printFriendsandNear(agentid,peoplelist,friendslist,nearlist) #Oppgave 1.3
        print()
        printNearbyFriends(agentid,friendslist,nearlist) #Oppgave 1.4
        print()
        printNewFriendSuggestion(agentid,peoplelist,friendslist) #Oppgave 1.5
        print()
        printTwoNearbyPeopleNotFriends(agentid,peoplelist,friendslist,nearlist) #Oppgave 1.6
        print()
    

if __name__ == '__main__':
    main()
