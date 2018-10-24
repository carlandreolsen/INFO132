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
	friendslist=[]
	for i in range(0,len(compiled_names)):
		try:
			print(compiled_names[i]+' har '+edgelist[i][1]+ ' venner.')
		except:
			print(compiled_names[i]+' har ingen venner.')


def main():
	nodefilename='noder_15_13.csv'
	edgefilename='kanter_15_13.csv'
	compiled_names = compile_names(nodefilename)
	compile_friends_list(compiled_names,edgefilename)

if __name__ == '__main__':
	main()


