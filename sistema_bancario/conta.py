from abc import ABC, abstractmethod


class Conta(ABC):
    """Representa uma conta bancária."""

    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def detalhes(self):
        print(f'Agência: {self.agencia} '
              f'Conta: {self.conta} '
              f'Saldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    """Representa uma conta poupança bancária."""

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    """Representa uma conta-corrente bancária."""

    def __init__(self, agencia, conta, saldo, limite=200):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente!')
            return

        self.saldo -= valor
        self.detalhes()
