class Passageiro:

    def __init__(self, user):
        self.__user = user
        self.__viagem = None

    def adicionar_pessoas(self, pessoas):
        pass

    def selecionar_destino(self, destino):
        pass

    def definir_hora(self, hora):
        pass

    def status_corrida(self):
        pass

    @property
    def viagem(self):
        return self.__viagem

    @viagem.setter  # agregação
    def viagem(self, viagem):
        self.__viagem = viagem

