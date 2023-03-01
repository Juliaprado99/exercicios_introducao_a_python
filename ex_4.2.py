# Escreva um programa que pergunte a velocidade do carro de um usuario.
# Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuario foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima do permitido.

# definição de variaveis

velocidade = int(input('Qual a velocidade do carro: '))
multa = 5

# if que vai verificar se usuario será multado

if velocidade > 80:
    valor = (velocidade - 80) * multa
    print(f'Você foi multado! O valor da multa é R$ {valor:,.2f}.')
else: 
    print('Parabens, você está dentro da velocidade permitida.')