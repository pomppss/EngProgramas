import matplotlib.pyplot as plt
import networkx as nx

class GerarGrafo():

    def gerar_grafo(self, raiz):
        G = nx.DiGraph()  
        self._adicionar_nos(G, raiz)
        return G
    
    def _adicionar_nos(self, G, no, parent=None):
        if no is None:
            return

        G.add_node(no.valor)

        if parent:
            G.add_edge(parent, no.valor)

        if no.esquerda:
            self._adicionar_nos(G, no.esquerda, no.valor)
        if no.direita:
            self._adicionar_nos(G, no.direita, no.valor)


    def desenhar_arvore(self, G):
        pos = self._posicionar_nos(G)
        plt.figure(figsize=(10, 8))

        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
        plt.title("Árvore Binária")
        plt.show()

    def _posicionar_nos(self, G):
        pos = {}
        def dfs(no, x=0, y=0, dx=1.0):
            pos[no] = (x, -y) 
            filhos = list(G.successors(no))
            if len(filhos) == 2:
                dfs(filhos[0], x - dx, y + 1, dx / 2)
                dfs(filhos[1], x + dx, y + 1, dx / 2)
            elif len(filhos) == 1:
                dfs(filhos[0], x, y + 1, dx / 2)

        raiz = [n for n in G.nodes if G.in_degree(n) == 0][0]
        dfs(raiz)
        return pos

