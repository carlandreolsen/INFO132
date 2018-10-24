def main():
	d0_a = {}
	d0_b = {}

	if d0_a == d0_b:
		print('%s er lik %s'%(d0_a,d0_b))

	d0_a= {True:False}
	d0_b['en'] = 1
	print('')

	if d0_a != d0_b:
		print('%s er ikke lik %s'%(d0_a,d0_b))

	print('d0_a inneholder %i element. Elementet inneholder en nøkkel og en verdi. "en" er nøkkel og verdi er "1".'%len(d0_a))

	print('Det går fortere å finne nøkler enn å finne verdier i en assosiativ liste. Pga. hashing av nøkler. Tar mer RAM enn en liste bygget opp på samme måte med 2 kolonner per rad')
	print('For hashe en liste eller et sett med unike verdier kan Set() metoden brukes. (from sets import Set)') 


	d9_int = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

	d9_str = {'tekst':123,'asdf':321,'qwer':234,'fwef':345,'sdfsdf':456,'fwefew':567,'gaga':678,'vavava':789,'fsdfs':890,'asvasdf231':135}

	for i in range(10):
		print(d9_int[i])

	l9_str = list(d9_str.values())
	for i in range(10):
		print(l9_str[i])
if __name__ == '__main__':
	main()