import random as rd
import numpy as np

class Dados:
    def __init__(self, n1: int) -> None:
        self.possibilidades=n1**2
        self.espaço_amostral = np.array([int(x) for x in range(2, n1 * 2 + 1)])
    
    def count(self,lista,procura):
        contagem=0
        for x in lista:
            if x==procura:
                contagem+=1
        return contagem
    
    def probabilidade(self,x) -> dict:
        if x<self.mediana_amostral():
            return (x-1) / self.possibilidades
        if x==self.mediana_amostral():
            return self.espaço_amostral[len(self.espaço_amostral)-1]/self.possibilidades/2
        else:
            return (len(self.espaço_amostral)-x+2)/self.possibilidades

    def probabilidade_mediana_amostral(self,x):
        self.probabilidade(self.mediana_amostral)

    def mediana_amostral(self):
        sorted_amostral = sorted(self.espaço_amostral)
        n = len(sorted_amostral)
        if n % 2 == 1:
            return sorted_amostral[n // 2]
        else:
            mediana=(sorted_amostral[n // 2 - 1]+sorted_amostral[n // 2])/2
            return mediana

    def dado(self) -> int:
        return rd.randint(1,self.possibilidades/2)
    
    def max(self) -> int:
        return f'{int(round(self.probabilidade(int(self.mediana_amostral()))*100,0))}%'
    
    def min(self):
        return f'{int(round(self.probabilidade(2)*100,0))}%'
dado=Dados(6)
print(dado.min(),dado.probabilidade(2))