print('--- Aplicativo de Cadastro de Veiculo ---')

print('--- Opções ---')

print('--- 1 - Cadastrar Veiculo ')
print('--- 2 - Consultar Veiculo')
print('--- 3 - Sair ')

value = 0

while( value != 3 ):
    
    value = int(input('Digite a sua opção: '))

    match value:
        case 1:
            print('Função de Cadastro')
        case 2:
            print('Função de Consulta')
        case 3:
            print('Função de Sair')
        case _:
            print('Função desconhecida')

print("Acabou")