"""
def split_all(the_list, sep):
	index = 0
	while index < len(the_list):
		line = the_list[index]
		the_list[index] = line.split(sep)
		index = index + 1
"""
#Funksjonen split_all går igjennom hver element i listen. 
#Om et element i listen inneholder tekststrengen sep vil det deles inn i flere elementer og erstatte sin egen posisjon.

from col020_oblig8_oppgave1 import check

#alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ\t'

def abbreviate(aList):
	for i in range(0,len(aList)):
		aList[i] = aList[i][0] 
	return aList	

def keep(the_list, target):
	the_new_list = []
	j=0
	for i in the_list:
		if i == target:
			the_new_list.append(the_list[j])
		j+=1
	return the_new_list

def main():
	filename = 'noder_50_50.csv'
	agents = 50
	if check(filename,agents) == None:
		my_file = open(filename,encoding='utf-8',mode='r')
		file_content = my_file.read()
		file_content = file_content.split('\n')
		list_of_content = []
		list_of_males = []
		list_of_females = []
		for i in file_content:
			list_of_content.append(i.split('\t'))

		list_of_content = abbreviate(list_of_content)
		list_of_females = keep(list_of_content,'female')
		femalecount = len(list_of_females)
		malecount = len(list_of_content)-femalecount
		print("There are %i females and %i males in the list."%(femalecount,malecount))

		#Antallet menn er det som var igjen av rader i list_of_content når antall kvinner ble trukket i fra.
	else:
		print(check(filename,agents))
if __name__ == '__main__':
	main()