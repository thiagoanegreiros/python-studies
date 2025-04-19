class VerificaSaudacao(type):
    def __init__(cls, name, bases, attrs):
        if 'saudacao' not in attrs or not isinstance(attrs['saudacao'], staticmethod):
            raise TypeError(f"A classe {name} deve ter um método estático chamado 'saudacao'")
        super().__init__(name, bases, attrs)

class MinhaClasse(metaclass=VerificaSaudacao):
    @staticmethod
    def saudacao():
        return "Oi, eu estou aqui!"
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_a_partir_ano_nascimento(cls, nome, ano_nascimento):
        idade = 2025 - ano_nascimento
        return cls(nome, idade)

    def __str__(self):
        return f'{self.nome}, {self.idade} anos'
