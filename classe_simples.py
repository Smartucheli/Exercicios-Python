class Veiculo:
    def __init__(self, cor, placa):
        self.cor = cor
        self.placa = placa
        
veiculo = Veiculo("Verde", 102030)
print(veiculo.cor)


class Cliente(): 
    def __init__(self, nome, email, carro):
        self.nome = nome
        self.email = email
        lista_carro = ["popular", "esportivo"]
        if carro in lista_carro:
            self.carro = carro
        else: 
            raise Exception("Plano inválido")

cliente = Cliente("Savio", "savio@gmail.com", "popular")
print(cliente.carro)   
    

