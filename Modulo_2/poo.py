# POO


# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        pass
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
    
# Objetos
pessoa1 = Pessoa("Pedro", 22)
mensagem = pessoa1.saudacao()
print(mensagem)