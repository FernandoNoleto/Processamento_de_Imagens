#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:31:32 2018

@author: thiago
"""

from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

def imprimir_matriz(matriz):
    print(np.asarray(matriz))

def matriz_da_imagem(img):
    return np.asarray(img.convert('L'))

def filtroLaplaciano(img):
    filtroA = [0,1,0,1,-4,1,0,1,0]
    matrizImagem = matriz_da_imagem(img)
    matrizNova = np.zeros((img.height, img.width), dtype=np.integer)
    for i in range(img.height - 2):
        for j in range(img.width - 2):
            matrizNova[i+1][j+1] = (matrizImagem[i][j] * filtroA[0] +
                                   matrizImagem[i][j+1] * filtroA[1] +
                                   matrizImagem[i][j+2] * filtroA[2] +
                                   matrizImagem[i+1][j] * filtroA[3] +
                                   matrizImagem[i+1][j+1] * filtroA[4] +
                                   matrizImagem[i+1][j+2] * filtroA[5] +
                                   matrizImagem[i+2][j] * filtroA[6] +
                                   matrizImagem[i+2][j+1] * filtroA[7] +
                                   matrizImagem[i+2][j+2] * filtroA[8])/9 
    return matrizNova
                    


def main():
    img = abrir_imagem("BolsoSimpson.jpg")   
    filtroImg = filtroLaplaciano(img)
    #filtroImg.show()
    #img.show()
    
    
    
    
    

    
if __name__ == '__main__':
    main()