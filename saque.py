from time import sleep
print('='*30)
banco = 'BRUBANK'
print(f'{banco:^30}')
print('='*30)
print('Limite do saque R$8.000,00')
valor = int(input('Qual valor deseja sacar? R$'))
total = valor
ced = 50
totced = 0
op = '?'

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            sleep(0.8)
            print("")
            print('Saque realizado! Volte sempre.')

            sleep(1)
            break

    if valor > 8000:
        valor = int(input('''Valor inválido. O limite é de R$8.000,00
        Qual valor deseja sacar? R$'''))

