
def montar_dic(inteiro, fatorial, divisores):
    analisados = {'fatorial': fatorial, 'divisores': divisores}
    
    return f'''
    O fatorial do numero {inteiro} é: {analisados['fatorial']}
    E os divisores do número {inteiro} são: {analisados['divisores']}
'''

def analisar_int():
    num = int(input('Digite o seu número inteiro a ser analisado: '))
    index = 1
    num_list = []


    # Cria a coloca todos os números anteriores ao número do input dentro de uma lista
    while index <= num:
        num_list.append(index)
        index+=1

    reverse_list = num_list[::-1]
    # Fatorial
    fatorial = 1
    for n in reverse_list:
        fatorial = fatorial*n

    # Divisores
    divisores = []
    for n in num_list:
        if num % n == 0:
            divisores.append(n)
    
    return num, fatorial, divisores

resultado = analisar_int()
print(montar_dic(*resultado))