# Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento. 
# Para salarios superiores a 1250, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.


# registrando o salario por meio de entrada num input e guardando numa variavel

salario = int(input(f'Informe o salario: '))

# if que defina o valor do aumento

if salario > 1250:
    salario_novo = salario * 1.1
    print(f'O novo salario com reajuste é R${salario_novo:,.2f}')
    
else:
    salario_novo = salario * 1.15
    print(f'O novo salario com reajuste é R${salario_novo:,.2f}')
    