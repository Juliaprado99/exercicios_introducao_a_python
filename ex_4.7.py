# Faça um programa que leia a categoria de um produto e determine o preço pela tabela.

#coletando categoria via input e guardando na variavel.

categoria = int(input('Qual a categoria do produto? '))


# com o if, será definido em qual categoria de preço o produto se encaixa

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    preco = 0
    print('Categoria invalida, tente novamente.')

print(f'O preço do produto é R${preco:,.2f}.')