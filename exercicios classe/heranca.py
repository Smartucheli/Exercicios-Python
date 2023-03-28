class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def Bonidicacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qnt_funcionarios):
        super().__init__(nome,cpf,salario)
        self._senha = senha
        self._qnt_funcionarios = qnt_funcionarios

        def Autentica(self, senha):
            if self._senha == senha:
                return print("Acesso Permitido!")
            else:
                return print("Acesso negado!")

gerente = Gerente("Savio", "22222222-30", 1200.00, "teste", 0)
print(gerente.Bonidicacao())
print(gerente._senha)