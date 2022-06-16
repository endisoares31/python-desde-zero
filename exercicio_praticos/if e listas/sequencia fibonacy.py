#programa para Mostrar a sequecia de fibonace

from netrc import NetrcParseError


def recur_fibon (n):
    if n <= 1:
        return n
    else:
        return(recur_fibon(n-1)+recur_fibon(n-2))
nterms = 10

# verificar se o numero terms é valido

if nterms <= 0:
    print ("por favor inserir o numero inteiro positivo")
else:
    print("Sequencia de Fibonace: ")
    for i in range(nterms):
        print(recur_fibon(i))
