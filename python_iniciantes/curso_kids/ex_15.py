# crie um programa que peca dois numeros para o usuário e a operacao que ele queira realizar e mostre o resultado da conta na tela

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segunndo numero: '))
op = input ('Digite \n[+] = Adicão \[-] = Subtracão \n[*] =  Multiplicacão \n[/] = Divisão\n')

if op not in '+,-,*,/ ':
	print('Operacão inválida ')
else:
	if op =='+':
		conta = num1 + num2
	elif op == '-':
		conta = num1 - num2
	elif op == '*':
		conta = num1 * num2
	elif op == '/':
		conta = num1 / num2
	print('{:.1f}'.format(conta))
		



