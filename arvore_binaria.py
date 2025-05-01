import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Função para criar a árvore binária a partir de um array
def array_para_bst(array):
    if not array:
        return None

    meio = len(array) // 2
    raiz = Node(array[meio])

    raiz.esquerda = array_para_bst(array[:meio])
    raiz.direita = array_para_bst(array[meio+1:])

    return raiz

# Função para gerar o grafo da árvore binária com NetworkX
def gerar_grafo(raiz):
    G = nx.DiGraph()  # Cria um grafo direcionado
    _adicionar_nos(G, raiz)
    return G

# Função auxiliar para adicionar nós ao grafo
def _adicionar_nos(G, no, parent=None):
    if no is None:
        return

    # Adiciona o nó
    G.add_node(no.valor)

    if parent:
        # Adiciona uma aresta entre o nó pai e o nó atual
        G.add_edge(parent, no.valor)

    # Chama recursivamente para os filhos esquerdo e direito
    if no.esquerda:
        _adicionar_nos(G, no.esquerda, no.valor)
    if no.direita:
        _adicionar_nos(G, no.direita, no.valor)

# Função para desenhar a árvore binária
def desenhar_arvore(G):
    pos = _posicionar_nos(G)  # Define as posições dos nós para a visualização
    plt.figure(figsize=(10, 8))

    # Desenha o grafo com os nós e as arestas
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    plt.title("Árvore Binária")
    plt.show()

# Função para posicionar os nós na tela de forma hierárquica
def _posicionar_nos(G):
    pos = nx.spring_layout(G, k=0.5, iterations=50)  # Posicionamento dos nós
    return pos

# Exemplo de uso
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
raiz = array_para_bst(array)

# Gera o grafo da árvore
grafo = gerar_grafo(raiz)

# Desenha a árvore
desenhar_arvore(grafo)
