alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ\t'
def check(filename, agents):
	try:
		nodesFile = open(filename, encoding='utf-8',mode='r')
	except:
		return "No file named %s found"%filename
	nodes = nodesFile.read()
	nodes = nodes.split('\n')
	row=""
	listOfNodes = []
	if len(nodes) != agents:
		nodesFile.close()
		return "Expected %i lines. Found %i"%(agents,len(nodes))
	for i in nodes:
		row = i.split('\t')
		if len(row) !=3:
			nodesFile.close()
			return "The line '%s' doesn't have three columns."%i
		for j in i:
			if j.capitalize() not in alfabet: 
				nodesFile.close()
				return "line '%s' contains the illegal character %s"%(i,j)
		listOfNodes.append(row)
	nodesFile.close()
	return None

def main():
	filename = 'noder_50_50_feil_4.csv'
	agents = 50
	print(check(filename,agents))
	#Check er også brukt i Oppgave 2.
if __name__ == '__main__':
	main()