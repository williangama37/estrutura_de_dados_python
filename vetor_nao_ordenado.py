import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
        
    def adicionar(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Apenas inteiros são permitidos.")
        if self.capacidade > self.ultima_posicao + 1:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
        else:
            print("Sem espaço no vetor")
            
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def remover(self, valor):
        posicao = self.pesquisar(valor)
        if posicao != -1:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            self.ultima_posicao -= 1
        else:
            print("Valor não encontrado")
    
    def imprimir(self):
        if self.ultima_posicao != -1:
            for i in range(self.ultima_posicao + 1):
                print(f"Index {i}, Valor {self.valores[i]}")
        else:
            print("Vetor vazio")
