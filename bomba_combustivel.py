class bomba_combustivel:

    def __init__(self, tipoComb, ValorL, quantComb):
        self.tipoComb = tipoComb
        self.ValorL = ValorL
        self.quantComb = quantComb

    def abastece_por_valor(self, valor):
        return valor / self.ValorL
        
        

    def abastece_por_litro(self, total):
        return total / self.quantComb

    def alterar_valor(self, valor):
        self.ValorL = valor
    
    def alterar_combustivel(self, comb):
        self.tipoComb = comb
    
