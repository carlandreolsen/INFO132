from network import Network

def fileToDict(filename):
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
    for i in range(0,len(my_list)): 
    	my_list[i][0] = int(my_list[i][0])
    	my_list[i][1] = int(my_list[i][1])
    my_dict = {}
    for i in my_list:
    	if i[0] in my_dict:
    		if i[1] in my_dict[i[0]]:
    			continue
    		else:
    			my_dict[i[0]].append(i[1])
    	else:
    		my_dict.update({i[0]:[i[1]]})
    	if i[1] in my_dict:
    		if i[0] in my_dict[i[1]]:
    			continue
    		else:
    			my_dict[i[1]].append(i[0])
    	else:
    		my_dict.update({i[1]:[i[0]]})
    return my_dict

def main():
	edgedict=fileToDict('nettverk_5_1_kanter')
	asdf = Network(edgedict)
	print(asdf.edges)
	asdf.add_edge(9,2)
	asdf.add_edge(4,7)
	asdf.add_edge(0,7)
	print(asdf.edges)
	print('Friends of agent 2: %s'%asdf.friends_of(2))
	print('Friends of agent 3: %s'%asdf.friends_of(3))
	print('Friends of agent 0, 1 & 2: %s'%asdf.friends_of_these([0,1,2]))


if __name__ == '__main__':
	main()