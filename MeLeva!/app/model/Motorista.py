class Motorista:

    def __init__(self, user):
        self.__user = user
        self.__viagem = None

    def iniciar_corrida(self, viagem):
        pass

    def terminar_corrida(self, viagem):
        pass

    def aceitar_corrida(self, viagem):
        pass

    def cancelar_corrida(self, viagem):
        pass

    def def_contribuicao(self, viagem):
        pass

    @property
    def viagem(self):
        return self.__viagem

    @viagem.setter  # agregação
    def viagem(self, viagem):
        self.__viagem = viagem
