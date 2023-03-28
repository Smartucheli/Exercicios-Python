class Conta:

    def __init__(self, num_conta, nome, saldo = 0):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome

    def deposito(self, deposito):
        self.saldo += deposito

    def saque(self, saque):
        if self.saldo == 0:
            return print(f"Impossivel realizar saque pois sua conta tem {self.saldo}$" )
        elif self.saldo < saque:
            return print(f'não foi possivel realizar o saque pois não tem saldo suficiente - sua conta tem {self.saldo}$')
        else:
            self.saldo -= saque

c1 = Conta(150, 'savio', 0)
c1.alterar_nome('Novela')
c1.deposito(20)
print(c1.saldo)
c1.saque(30)

