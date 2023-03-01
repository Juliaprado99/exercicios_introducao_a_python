# Escreva um prograna que leia 2 numeros e pergunte qual operação você deseja realizar, com as 4 operações matematicas. 
# Exiba o resultado da operação.

#coletando os numeros via input e guardando nas variaveis.

num1 = float(input('Numero 1: '))
num2 = float(input('Numero 2: '))

# input que recebe o numero referente a operação que o usuario deseja realizar.

operacao = int(input('Qual operação deseja realizar? \n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão'))

#If que realiza as operações

if operacao == 1:
    result = num1 + num2
elif operacao == 2:
    result = num1 - num2
elif operacao == 3:
    result = num1 * num2
elif operacao == 4:
    result = num1 / num2
else: 
    print('Operação invalida, tente novamente.')
    result = 'Invalido'
print(f'O resultado é {result}.')



    