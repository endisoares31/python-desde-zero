"""
Considere uma empresa de telefonia Tchau.
Abaixo de 200 minutos a empresa cobra R$ 0.20 por minutos. 
Entre 200 e 400 minutos o preco é de R$0.18. Acima de 400 minutos o preco por minutos é de R$ 0.15
Calcula a sua conta de telefone

"""
minutos = int(input("Minutos: "))
if minutos < 200:
    preco = 0.2
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08
print(f'R$ {preco*minutos:.2f}')
