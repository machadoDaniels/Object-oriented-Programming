class User:
    def __init__(self, nome, password, email, num_matricula, data_nasc, telefone, endereco, score):
        self.nome = nome
        self.password = password
        self.email = email
        self.num_matricula = num_matricula
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.endereco = endereco
        self.score = score
        self.password = password
        self.email = email

    def verif_login(self, email, password):
        return self.email == email and self.password == password

    def verif_matricula(self, num_matricula):
        return self.num_matricula == num_matricula

    def login(self):
        pass

    def autualizar_perfil(self):
        pass

    def avaliar(self):
        pass

    def def_modo(self):
        pass
