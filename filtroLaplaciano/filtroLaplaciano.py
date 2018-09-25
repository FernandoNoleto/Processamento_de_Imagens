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

def escala_de_cinza(img):
    return img.convert('L')

def filtroLaplaciano(img):
    #filtroA = [0,1,0,1,-4,1,0,1,0]
    #filtroB = [1,1,1,1,-8,1,1,1,1]
    #filtroC = [0,-1,0,-1,4,-1,0,-1,0]
    filtroA = [-1,-1,-1,-1,8,-1,-1,-1,-1]
    new_img = Image.new('L', (img.width, img.height), color = 'black')
    pix = img.load()
    new_pix = new_img.load()
    for i in range(img.height - 2):
        for j in range(img.width - 2):
            valor = int((pix[i,j] * filtroA[0] +
                                   pix[i,j+1] * filtroA[1] +
                                   pix[i,j+2] * filtroA[2] +
                                   pix[i+1,j] * filtroA[3] +
                                   pix[i+1,j+1] * filtroA[4] +
                                   pix[i+1,j+2] * filtroA[5] +
                                   pix[i+2,j] * filtroA[6] +
                                   pix[i+2,j+1] * filtroA[7] +
                                   pix[i+2,j+2] * filtroA[8])/9)
            if valor < 0:
                new_pix[i+1,j+1] = 0
            elif valor > 255:
                new_pix[i+1,j+1] = 255
            else:
                new_pix[i+1,j+1] = valor
    
    for i in range(img.height):
        for j in range(img.width):
            if(i == 0):
                new_pix[i,j] = pix[i,j]
            if(j == 0 and i > 0):
                new_pix[i,j] = pix[i,j]
            if(i == img.height):
                new_pix[i,j] = pix[i,j]
            if(j == img.width):
                new_pix[i,j] = pix[i,j]
    
    return new_img
                    


def main():
    img = abrir_imagem("BolsoSimpson.jpg")
    img = escala_de_cinza(img)
    img.show()
    img = filtroLaplaciano(img)
    img.show()
    
        
if __name__ == '__main__':
    main()