'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
SETEMBRO DE 2018
'''

from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from itertools import product
import math, random

#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

#Converte a imagem para escala de cinza
def escala_de_cinza(img):
    return img.convert('L')

def gerar_matriz (n_linhas, n_colunas):
    matriz = np.zeros((n_linhas, n_colunas), dtype=np.str)
    return matriz

def imprimir_matriz(matriz):
    print(np.asarray(matriz))

def matriz_da_imagem(img):
    return np.asarray(img.convert('L'))

#Passar a imagem já na escala de cinza
def histograma(img):
    
    width, height = img.size
    # pix = img.load()
    pix = [[4, 4, 3, 3],
        [4, 4, 3, 3],
        [4, 1, 2, 3],
        [0, 1, 2, 3]]
    escala = 0
    #Obtendo os níveis de cinza da imagem
    # for y, x in product(range(height), range(width)):
    #     if pix[x,y] > escala:
    #         escala = pix[x,y]
    # escala += 1
    # print(escala)
    escala = 8

    rk = {}
    nk = {}
    prrk = {}
    freq = {}
    eq = {}
    rk_arredondado = {}
    img_equalizada = []
    # tam_imagem = height*width
    tam_imagem = 16
    count = 0
    

    for i in range(escala):
        rk[i] = i
    
    #Obtendo o nk    
    for v in rk.values():
        for y, x in product(range(height), range(width)):
            if (pix[x][y] == v):
                count += 1
        
        nk[v] = count
        count = 0
    # print (nk)
    
    
    
    #Obtendo o prrk
    for k,v in nk.items():
        prrk[k] = v/tam_imagem
    print(prrk)

    #Obtendo a freq


    

    return img_equalizada


def main():
    img = abrir_imagem("4x4.png")
    img = escala_de_cinza(img)
    # img.save('binarized_img.png')
    # opc = int(input('Alguma escala especifica? 0 para default = 255:. '))
    img = histograma(img)
    

    



if __name__ == '__main__':
    main()
    # aux = 10
    # data = {}
    # for x in range(aux):
    #     data[x] = x
    # print(data)
    # print(type(aux))
    
