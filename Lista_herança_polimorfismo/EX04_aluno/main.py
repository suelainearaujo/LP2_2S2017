from aluno import *

aluno = Aluno(input("Qual o nome do aluno? :"),input("Qual o seu curso? :"),int(input(" Esta quanto tempo sem dormir ? : ")))
aluno.Estudar(int(input("Quantas horas voce estuda ? :")))
dormir = aluno.Dormir(int(input("Quantas horas voce Dorme ? :")))
print(" Voce esta {}Hs sem dormir" .format(dormir))
