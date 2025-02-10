class carro:
    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.cor = ''
        self.placa = ''


    def adicionar_marca(self, marca):
        self.marca = marca
        
    def adicionar_modelo(self, modelo):
        self.modelo = modelo

    def adicionar_cor(self, cor):
        self.cor = cor

    def adicionar_placa(self, placa):
        self.placa = placa

    def escrever_marca(self):
        print(f'Marca: {self.marca}')
        
    def escrever_modelo(self):
        print(f'Modelo: {self.modelo}')

    def escrever_cor(self):
        print(f'Cor: {self.cor}')

    def escrever_placa(self):
        print(f'Placa: {self.placa}')

class carros:
    def __init__(self):
        self.cadastrados = []

    def adicionar_carro(self, carro):
        self.cadastrados.append(carro)

    def consultar_carro(self):
        for carro in self.cadastrados:
            carro.escrever_marca()
            carro.escrever_modelo()
            carro.escrever_cor()
            carro.escrever_placa()
            print('')