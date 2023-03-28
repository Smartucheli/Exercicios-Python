class quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudar_Vlado(self, lado):
        self.lado = lado

    def imprime_lado(self):
        print(self.lado)

    def area(self, lado):
        return lado * lado

Q1 = quadrado(20)
Q1.mudar_Vlado(10)
Q1.imprime_lado()
x = Q1.area(20)
print(x)