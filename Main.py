from Carros import carros, carro

print('--- Aplicativo de Cadastro de Veiculo ---')

print('--- Opções ---')

print('--- 1 - Cadastrar Veiculo ')
print('--- 2 - Consultar Veiculo')
print('--- 3 - Sair ')

value = 0
_lista_de_carros = carros()

while( value != 3 ):

    print('')
    value = int(input('Digite a sua opção: '))
    print('')

    match value:
        case 1:
            _carro = carro()
            _carro.adicionar_marca(input('Digite a Marca: '))
            _carro.adicionar_cor(input('Digite a Cor: '))
            _carro.adicionar_modelo(input('Digite a Modelo: '))
            _carro.adicionar_placa(input('Digite a Placa: '))

            _lista_de_carros.adicionar_carro(_carro)

            print('')
            print('Cadastrado com Sucesso')
            print('')

        case 2:
            print('Lista de Carros')
            print('')

            _lista_de_carros.consultar_carro()
            
        case 3:
            print('Função de Sair')
        case _:
            print('Função desconhecida')

print("Acabou")