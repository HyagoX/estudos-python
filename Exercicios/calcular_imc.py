# Tabela IMC
# Abaixo de 19.1: Abaixo do peso
# Entre 19.1 e 25.9: Peso normal
# Entre 25.9 e 27.3: Pouco Acima do peso
# Entre 27.3 e 32.3: Acima do peso
# Acima de 32.4: Obesidade
# Fórmula do IMC: Peso / (altura * altura)

def calculoIMC(height, weight):
    return weight/(height * height)

def classificar_imc(imc):
    if imc < 19.1:
        return f'Seu IMC é: {imc}: Voce está abaixo do peso'
    elif imc > 19.1 and imc < 25.8:
        return f'Seu IMC é: {imc}: Voce está no peso normal'
    elif imc > 25.9 and imc < 27.3:
        return f'Seu IMC é: {imc}: Voce está pouco acima do peso'
    elif imc > 27.4 and imc < 32.3:
        return f'Seu IMC é: {imc}: Voce está acima do peso'
    else:
        return f'Seu IMC é: {imc}: Voce é Obeso'


height = float(input('Digite o sua altura: '))
weight = float(input('Digite seu peso: '))

imc = calculoIMC(height, weight)
classificacao = classificar_imc(imc)

print(classificacao)