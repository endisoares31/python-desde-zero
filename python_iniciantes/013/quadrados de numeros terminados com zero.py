"""
Dada a sequencia de numeros inteiros nao nulos,
seguidos por 0, imprimir seus quadrados
"""
n = int(input("Digite o primeiro numero: "))
while n != 0:
    print(n, "ao quadrado =", n*n)
    n = int(input("Digite o proximo numero: "))