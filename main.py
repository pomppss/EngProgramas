from src.algoritmos import ArvoreBinaria
from src.algoritmos import ArvoreBinariaTrivial
from src.utils import GerarGrafo
import time

def medir_tempo_trivial(array):
    arvore_trivial = ArvoreBinariaTrivial()
    inicio = time.time()
    arvore_trivial.array_to_bst_trivial(array)
    fim = time.time()
    return fim - inicio

def medir_tempo_divisao_conquista(array):
    arvore = ArvoreBinaria()
    inicio = time.time()
    arvore.array_para_bst(array)
    fim = time.time()
    return fim - inicio

if __name__ == "__main__":
    tamanhos = [50, 500, 1_000, 5_000, 10_000, 50_000]

    print(f"{'Tamanho (n)':<15}{'Trivial (s)':<15}{'Divisão e Conquista (s)':<25}")
    print("-" * 55)

    for n in tamanhos:
        array = list(range(1, n + 1))

        tempo_trivial = medir_tempo_trivial(array)
        tempo_divconq = medir_tempo_divisao_conquista(array)

        print(f"{n:<15}{tempo_trivial:.4f}{'':<5}{tempo_divconq:.4f}")






