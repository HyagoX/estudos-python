# Exercicio simples, recebemos uma lista de números, e então contamos quantas vezes certo número aparece na lista

numbers = (input('Type 10 numbers separated with space: '))
count = int(input('Which number you want to count?: '))

numbers_split = numbers.split( )
counter = 0

for n in numbers_split:
    print(n)
    n = int(n)
    if n == count:
        counter = counter + 1

print(f'Your number appears {counter} times')


