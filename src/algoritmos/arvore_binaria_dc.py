
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:

    def array_para_bst(self, array):
        if not array:
            return None

        meio = len(array) // 2
        raiz = Node(array[meio])

        raiz.esquerda = self.array_para_bst(array[:meio])
        raiz.direita = self.array_para_bst(array[meio+1:])

        return raiz
