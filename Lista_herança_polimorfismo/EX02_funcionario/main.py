from funcionario import Funcionario

funcionario = Funcionario(input("Qual nome do Funcionario? : "),int(input("Qual seu salario dele :")))

asalario = funcionario.AumentaSalario(int(input('qual sera o aumento dele ?  em % :')))

print(" O novo salario sera de R${}" .format(asalario))