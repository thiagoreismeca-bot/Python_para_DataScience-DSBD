
'''
Estruturas condicionais if, elif, else

'''

n1 = int(input('Digite o numero n1: ')) # armazena o numero n1
n2 = int(input('Digite o numero n2: ')) # armazena o numero n2

if n1>n2:
    print(f'O numero {n1} é maior do que {n2}')


elif n2>n1:
    print(f'O numero {n2} é maior do que {n1}')

else:
    print(f'Os numeros {n1} e {n2} são iguais')