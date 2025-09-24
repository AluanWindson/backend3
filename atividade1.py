class imagem:
    def __init__(self,nome,ano):
        self.nome = nome
        self.ano = ano

    def exibir(self):
        print(f"A imagem: {self.nome} está sendo exibida no ano de {self.ano}")

#Teste de classe da imagem
imagem1 = imagem("Museu do amanhã", 2024)     

#Método de clase(usa CLS)
#Não precisa da criação de instância

@classmethod

def mudar_nome(cls,nome_novo):
    cls.nome = nome_novo
    print(f"Agora o nome da imagem é: {cls.nome}, o museu futurístico")

#Método escrito(não usa SELF nem CLS)    
#Acesso - Não precisa da criação de instância
#Escopo - Não recebe o SELF nem o CLS, então não tem acesso.
#Caso queira acessar os da Classe poderá, porém terá que passar explicitamente

@staticmethod
def calcular_idade_imagem(ano_imagem, ano_atual):
    return ano_atual - ano_imagem