# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia eletrica. 
# Pergunte a quantidade de kWh consumida  o tipo de instalação.
# R para residencias, I para industrias, e C para comercios.
# Calcule o preco de acordo com a tabela.

# Lendo o consumo atraves de unput

consumo = float(input('Digite o consumo: '))

# lendo o tipo de instalação do local 

inst = input('Informe o tipo de instalação: \nR - Residencias\nI - Industrias\nC - Comercio')

# IF que verifica o tipo d einstalção e realiza o calculo de acordo 

if inst == 'R':
    if consumo <= 500:
        preco = consumo * 0.4
    else: 
        preco = consumo * 0.65
        
elif inst == "I":
    if consumo <= 5000:
        preco = consumo * 0.55
    else: 
        preco = consumo * 0.60
        
elif inst == "C":
    if consumo <= 1000:
        preco = consumo * 0.55
    else: 
        preco = consumo * 0.60

else:
    preco = 'Invalido'
    print('Instalação invalida. ')
    
print(f'O valor do consumo é R${preco:,.2f}')