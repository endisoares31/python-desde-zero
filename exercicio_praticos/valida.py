def digitefloat(n='Digite um número real: '):
    """
    Função que aceita somente números reais (float), aceita números com vírgula.
    :param n: informar o número.
    :return: Retorna um valor real.
    """
    while True:
        try:
            num = str(input(n)).strip().replace(',', '.')
            final = float(num)
            return final
        except ValueError:
            print('Digite sua altura em números separados por vírgula!')
            continue
        except Exception as erro:
            print(f'Infelizmente tivemos o erro: {erro.__class__}')