# Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em KM. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200km, e R$ 0,45 para viagens mais longas.

#coletando distancia via input e guardando na variavel.

distancia = float(input('INFORME A DISTANCIA: '))

# if que avalia o valor da kilometragem de acordo com a distancia

if distancia > 200:
    preco = distancia * 0.45
    print(f'O valor da passagem é {preco:,.2f}')
    
else:
    preco = distancia * 0.5
    print(f'O valor da passagem é {preco:,.2f}')

