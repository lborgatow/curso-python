class Pessoa:
    """Representa uma pessoa."""

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    """Representa um cliente de um sistema bancário."""

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta
