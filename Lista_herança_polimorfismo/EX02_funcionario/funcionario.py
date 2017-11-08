class Funcionario():

    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def AumentaSalario(self,Per_salario):
        self.Per_salario = ((self.salario*Per_salario)/100)+self.salario
        return self.Per_salario