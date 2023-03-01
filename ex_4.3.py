# Escreva um prorama que leia 3 numeros e que imprima o maior e o menor

#lendo os numeros por meio de input
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Terceiro numero: '))

# estrutura if aninhada que vai printar os numeros maior e menor

if num1 > num2 and num1 > num3:
    print(f'O maior numero é {num1}')
    if num2 > num3:
        print(f'O menor é numero {num3}')
    else:
        print(f'O menor é numero {num2}')
        
elif num2 > num1 and num2 > num3:
    print(f'O maior numero é {num2}')
    if num3 > num2:
        print(f'O menor é numero {num2}')
    else:
        print(f'O menor é numero {num3}')
elif num3 > num1 and num3 > num2:
    print(f'O maior numero é {num3}')
    if num1 > num2:
        print(f'O menor numero é {num2}')
    else:
        print(f'O menor numero é {num1}')
