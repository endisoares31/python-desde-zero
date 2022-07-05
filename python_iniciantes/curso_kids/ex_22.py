# Faca um programa que leia produtos de um mercado até que a entrada de dados seja "fim" (que nao deve ser armazenado).
#  por fim mostre a lista para o usuário.

lista = []
num_item = 1

while (True):
	item = input('Qual o {}º item:\n'.format(num_item))
	num_item = num_item + 1 
	lista.append(item)
	print(lista)
	if (item == 'fim'):
		print ('Aqui está a sua lista')
		break
	else:
		lista.append(item)
print(lista)
		
