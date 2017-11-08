class Triangulo():
    def __init__(self,ladoA,ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calculo_perimetro(self):
        perimetro = self.ladoA + self.ladoB +self.ladoC
        return perimetro

    def getMaior(self):
        if (self.ladoA > self.ladoB) or (self.ladoA > self.ladoC):
            return print('Lado A é maior')
        elif (self.ladoB > self.ladoA) or (self.ladoB  > self.ladoC):
            return print('lado B é maior')
        elif (self.ladoC  > self.ladoA) or (self.ladoC  > self.ladoB):
            return print('lado B é maior')

