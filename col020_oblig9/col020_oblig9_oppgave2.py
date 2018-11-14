def compile_names(nodefilename):
	nodefile = open(nodefilename, encoding='utf-8',mode='r')
	nodefilecontent = nodefile.read()
	nodefile.close()
	nodefilecontent = nodefilecontent.split('\n')
	nodelist = []
	for i in nodefilecontent:
		nodelist.append(i.split('\t'))
	filter_nodedict = {}
	for i in range(0,len(nodelist)):
			filter_nodedict.update({i : nodelist[i][1] + ' ' + nodelist[i][2]})
	return filter_nodedict

def compile_friends_list(compiled_names, edgefilename):
	edgefile = open(edgefilename, encoding='utf-8',mode='r')
	edgefilecontent = edgefile.read()
	edgefile.close()
	edgefilecontent = edgefilecontent.split('\n')
	edgelist=[]
	for i in edgefilecontent:
		edgelist.append(i.split('\t'))
	friendslist={}	
	for k,v in compiled_names.items():
		i = 0
		for j in range(0,len(edgelist)):
			if int(edgelist[j][0]) == k or int(edgelist[j][1]) == k:
				i+=1 #Teller opp en for hver forkomst av en persons nøkkel/id.
		friendslist.update({v:i})
	return friendslist

def main():
	nodefilename='noder_15_13.csv'
	edgefilename='kanter_15_13.csv'
	compiled_names = compile_names(nodefilename)
	print(compile_friends_list(compiled_names,edgefilename))

if __name__ == '__main__':
	main()


