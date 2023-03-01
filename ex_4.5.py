# Um programa que de acordo com a idade do carro, define se ele é novo ou velho. 
# Se tiver idade igual ou menor a 3, é novo. 
# Se tiver idade maior que 3, é velho.

#coletando idade do carro via input e guardando na variavel.

idade_carro = int(input('Digite a idade do seu carro: '))

# if que define se carro é velho ou novo

if idade_carro <= 3:
    print('O seu carro é novo.')
else:
    print('O seu carro é velho.')

