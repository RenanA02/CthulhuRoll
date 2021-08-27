import random;
import os;

def roll():
	rolagem = random.randint(1,20)
	'''rolagem = 19'''
	return(rolagem)

def veroll(num,nump):
	todo = nump
	metade = round(todo/2)
	quinto = round(todo/5)
	
	if(metade>todo/2):
		metade = metade-1
	if(quinto>todo/5):
		quinto = quinto-1
	print(todo,metade,quinto)
	
	if(num==1):
		return('Desastre D:')
	elif(quinto+num>=21):
		return('Extremo!!!')
	elif(metade+num>=21):
		return('Bom')
	elif(todo+num>=21):
		return('Normal')
	else:
		return('Fracasso')
		
	

resposta = 's'
while(resposta=='s'):
	d20 = roll()
	pericia = int(input('numero da pericia: '))
	dados = pericia
	resultado = veroll(d20,dados)

	print('Rolagem = ',d20)
	print('>>',resultado,'<<')
	
	resposta=str(input('De novo?: ' ))
	os.system('cls')

