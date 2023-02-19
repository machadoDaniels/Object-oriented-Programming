class Veiculo:

    def __init__(self, modelo, placa, ano, cor, motorista):
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
        self.__cor = cor
        self.__motorista = motorista

    def editar_dados_veiculo(self, modelo, placa, ano, cor):
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
        self.__cor = cor

    def __del__(self):
        print("Veiculo deletado!")
