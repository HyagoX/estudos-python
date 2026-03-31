try:
    numero = int(input('Digite um número: '))
    print(f'Voce digitou: {numero}')
except(ValueError):
    print('Digite números, nao letras')
# else:
#     print('Deu problema')
# Finally é executado independente de ter algum erro ou não
finally:
    print('Terminou a execução')