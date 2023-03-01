# Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
# O programa deve perguntar o valor da casa, o salario e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salario.
# Calcule o valor da prestação como sendo o valor da casa a comprar, dividido pelo numero de meses.

# Obtendo o salario por meio de input

salario = float(input('Valor do salario: '))
anos = int(input('Quantos anos pretende pagar:  '))
casa = float(input('Valor da casa: '))

# definição das variaveis meses e parcelas

meses = anos * 12
parcelas = casa / meses

# if com a definição de aprovação

if salario * 0.3  > parcelas:
    print(f'Foi aprovado! O valor será de R${parcelas:,.2f}, pago em {meses} meses.')
else:
    print('Infelizmente seu emprestimo não foi aprovado.')
