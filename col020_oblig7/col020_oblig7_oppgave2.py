import traceback

def read_csv_to_list(filename):
	try:
		file = open(filename)
	except:
		print('File not found with name "'+filename+'".')
		return False	
	content = file.read()
	file.close()
	rowsofcontent = content.split('\n')
	listofcontent=[]
	for i in rowsofcontent:
		listofcontent.append(i.split('\t'))
	return listofcontent
	
def main():
	while 1:
		try:	
			netsize = input('Størrelse: ')
			netid = input('Nettverks-ID: ')
			agentid = input('Agent-ID: ')
			edges = read_csv_to_list('kanter_'+netsize+'_'+netid+'.csv')
			if not edges:
				continue
			friendcount = 0
			for i in edges:
				if i[0] == agentid:
					friendcount +=1
			if friendcount == 0:
				print('Agent '+agentid+' is not found in the network.')
			else:
				print('Agent '+agentid+' has '+str(friendcount)+' friends.')
		except:
			traceback.print_exc()

if __name__ == '__main__':
	main()