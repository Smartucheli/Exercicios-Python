class Pessoa:
    
    def __init__(self, peso, idade, altura, nome):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.altura = altura

    
    def envelhece(self, anos):
        antes = self.idade
        conta = (21-antes) * 0.5
        conta2 = anos * 0,5
        self.idade += anos
        if(antes < 21):
            self.cresce(conta2)
        else:
            self.crece(conta)

    def engorda(self, peso):
        self.peso += peso
    
    def emagrece(self, peso):
        if(self.peso < peso):
            self.peso = 0
        else:
            self.peso -= peso
    
    def cresce(self, altura):
        self.altura += altura

savio = Pessoa(65, 20, 180, 'Savio')
print(vars(savio))
savio.engorda(1)
print(vars(savio))
savio.emagrece(2)
print(vars(savio))
savio.cresce(1)
print(vars(savio))
savio.envelhece(2)
print(vars(savio))