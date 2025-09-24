class imagem:
    def __init__(self,nome,ano):
        self.nome = nome
        self.ano = ano

    def exibir(self):
        print(f"A imagem: {self.nome} está sendo exibida no ano de {self.ano}")

#Teste de classe da imagem
imagem1 = imagem("Museu do amanhã", 2024)     

imagem1.exibir()