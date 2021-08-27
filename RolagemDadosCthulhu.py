import random

def roll():
	rolagem = random.randint(1,100)
	return(rolagem)

def veroll(num,nump):
	inteiro = nump
	metade = round(nump/2)
	quinto = round(nump/5)
	
	if(metade>nump/2):
		metade = metade-1
	if(quinto>nump/5):
		quinto = quinto-1
	print(inteiro,metade,quinto)
	
	if(num==100):
		return('Desastre D:')
	elif(num<=quinto):
		return('Extremo!')
	elif(num<=metade):
		return('Bom')
	elif(num<=inteiro):
		return('Normal')
	else:
		return('Falha :(')
	
	
d100 = roll()
pericia = int(input('numero da pericia: '))
dados = pericia
resultado = veroll(d100,dados)

print('Rolagem = ',d100)
print('>>',resultado,'<<')


