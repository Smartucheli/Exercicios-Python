class retangulo:

    def __init__(self, base, altura):
        self.setbase(base)
        self.setaltura(altura)

    def setaltura(self, altura):
        self.altura = altura
    
    def getaltura(self, altura):
        return self.altura

    def setbase(self, base):
        self.base = base
    
    def getbase(self, base):
       return self.base 

    def area(self):
        return self.altura * self.base
        
    
    def perimetro(self):
        return 2*self.altura + 2*self.base
    

base = int(input('Informe a base: '))
altura = int(input("Informe a altura: "))
r1 = retangulo(base, altura)
print("A area do retangulo é %d" % r1.area())
print("E o perimetro do retangulo é: %d" % r1.perimetro())
