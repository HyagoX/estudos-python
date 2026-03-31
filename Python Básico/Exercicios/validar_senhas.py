# Validador de senha
# Regras: 
# 1. A senha deve ter no mínimo 8 Caracteres
# 2. A senha, nao pode ser '12345678'
# O resultado esperado é dizer se a senha é valida ou não

while True:
    verified_password = input('Register your password: ')
    if verified_password == '12345678':
        print('The password cannot be 12345678, change it!')
    elif verified_password < 8:
        print('Too small!') 
    else:
        break

while True:
    user_password = input('Type your password: ')
    if user_password == verified_password:
        print('Acess granted')
        break
    else:
        print('Incorrect Password! Please try again')

