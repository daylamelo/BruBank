from time import sleep
print('Bem-Vindo ao BruBank! Vamos iniciar seu cadastro...')
sleep(1)
Nome = input('Nome completo: ')
while True:
    idade = int(input('Idade: '))
    if idade < 18:
        print(f'Olá {Nome}. Você ainda é menor de idade, infelizmente não poderemos dar continuidade ao seu cadastro.')
        break
    if idade > 120:
        print('\033[0;31mUma pessoa dessa idade provavelmente estaria falecida. Você está tentando nos enganar, encerramos aqui!!\033[m')
        break

    sexo = '?'
    while sexo not in 'MF':
        sexo = str(input('Sexo (M/F): ')).strip().upper()[0]


    cidade = input('Em qual cidade você mora? ')

    print('Parabéns, cadastro realizado com sucesso, em um prazo de 5 dias estaremos enviando seu cartão de crédito :D')

    resp = '?'
    while resp not in 'SN':
        resp = str(input('Deseja se cadastrar novamente? (S/N)  ')).strip().upper()[0]
    if resp == 'N':
        break

