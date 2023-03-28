class tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    
    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
    
    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
    
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
    
    def retorna_dados(self):
        return f'o tamagushi tem nome {self.nome}, idade {self.idade}, saúde{self.saude} e sua fome é {self.fome}'

    def humor(self):
        if(self.fome == "muita" & self.saude == "ruim"):
            return f'ele esta com humor: bravo'
        elif(self.fome == "media" & self.saude == "ruim"):
            return f'ele esta com humor: meio bravo'
        elif(self.fome == "tranquila" & self.saude == "ruim"):
            return f'ele esta com humor: neutro'
        else:
            return f'ele esta com humor: bacana'