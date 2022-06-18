from rich import print 


# CONSTANTES
VOTOS_BOLSONARO = 0
VOTOS_LUTA = 1 

#roda eternamente
while True:
    #apresenta os candidados
    print('*'*20)
    print(f'TOTAL_BOLSONARO:{VOTOS_BOLSONARO}{os.linesep} TOTAL_LUTA:{VOTOS_LUTA}')
    print('*'*20)
#pemita votar
try:
    voto = int(input(f'para quem gostaria de votar?{os.linesep}1 -Bolsonaro{os.linesep}2-Lula{os.linesep}seu voto: '))
    #loop
    if voto == 1:
        VOTOS_BOLSONARO += 1
    elif voto == 2:
        VOTOS_LUTA += 1
    else:
        pass
except:
    print('Digite apenas 1 ou 2')
os.system('cls') 