class Viagem:

    def __init__(self, hora_inicio, hora_fim, data_inicio, data_fim, origem, destino, rota, valor):
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__origem = origem
        self.__destino = destino
        self.__rota = rota
        self.__valor = valor

    def infos_viagem(self):
        pass

    def gerar_mapa(self):
        pass

    def __del__(self):
        print("Viagem finalizada!")
