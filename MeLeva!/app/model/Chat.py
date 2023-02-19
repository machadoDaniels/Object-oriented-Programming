class Chat:

    def __init__(self, user1, user2):
        self.__user1 = user1
        self.__user2 = user2
        self.__mensagens = []

    @property
    def mensagens(self):
        return self.__mensagens

    @mensagens.setter
    def mensagens(self, mensagem_e_destino):
        self.__mensagens.append(mensagem_e_destino)