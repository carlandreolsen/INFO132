alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

def legal_filename(text):
	for i in text:
		if i not in alphabet:
			return False
	return True

def write_message(filename):
	myfile = open(filename,'w')
	print('type the input of your file. ** to end session.')
	while 1:
		texttofile = input()
		if texttofile == '**':
			break
		myfile.write(texttofile+'\n')
	myfile.close()

def main():
	userinputfilename = input('Enter filename')
	if legal_filename(userinputfilename):
		userinputfilename = userinputfilename+'.txt'
		write_message(userinputfilename)

if __name__ == '__main__':
	main()