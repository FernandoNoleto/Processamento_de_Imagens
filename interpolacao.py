import numpy as np
from random import randint


def vizinho_mais_proximo_reducao(matriz, tam):
    
    nova_matriz = []
    x = 0
    y = 0

    for i in range(tam/2):
        linha = []
        for j in range(tam/2):
            linha.append(matriz[y][x])
            x += 2
        x = 0
        y += 2
        nova_matriz.append(linha)
    
    return nova_matriz

def vizinho_mais_proximo_ampliacao(matriz, tam):
    pass

def popular_matriz_inicial(tam):

    matriz = []
    for i in range(tam):
	    linha = []
	    for j in range(tam):
	        linha.append(randint(1,100))
	    matriz.append(linha)
	
    return matriz

def imprimir_matriz(matriz):

    print(np.matrix(matriz))
    


if __name__ == "__main__":
    tam = input("Digite o tamanho da matriz (par):. ")
    
    matriz = popular_matriz_inicial(tam)
    print('Matriz original: ')
    imprimir_matriz(matriz)
    nova_matriz = vizinho_mais_proximo_reducao(matriz, tam)
    print('Matriz reduzida (Vizinho mais proximo): ')
    imprimir_matriz(nova_matriz)