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

def nova_imagem(img):
    new_img = Image.new('L', (img.width, img.height), color = 'black')
    # new_img.save('nova_imagem.png')
    # new_img.show()
    return new_img

def filtro_media(img):
    new_img = nova_imagem(img)
    pix = img.load()
    new_pix = new_img.load()
    
    for i in range(img.height):
        for j in range(img.width):
            if i > 0 and j > 0 and i < img.height-1 and j < img.width-1:
                new_pix[i,j] = int((pix[i-1,j-1] + pix[i-1, j] + pix[i-1, j+1] +
                                    pix[i,j-1]   + pix[i, j]   + pix[i, j+1] +
                                    pix[i+1,j-1] + pix[i+1, j] + pix[i+1, j+1]) / 9)
    
    #Replicação dos pixels da borda
    
    #Canto superior esquerdo
    new_pix[0,0] = new_pix[1,1]
    #Canto inferior esquerdo
    new_pix[0,new_img.width-1] = new_pix[1,new_img.width-2]
    #Canto superior direito
    new_pix[new_img.width-1,0] = new_pix[new_img.width-2,1]
    #Canto inferior direito
    new_pix[new_img.width-1,new_img.height-1] = new_pix[new_img.width-2,new_img.height-2]

    # Primeira linha
    for j in range(1, img.width-1, 1):
        new_pix[j, 0] = new_pix[j,1]
    
    # Última linha
    for j in range(1, img.width-1, 1):
        new_pix[j, img.height-1] = new_pix[j,img.height-2]
    
    #Primeira coluna
    for i in range(1, img.height-1, 1):
        new_pix[0, i] = new_pix[1,i]
    
    #Última coluna
    for i in range(1, img.height-1, 1):
        new_pix[img.width-1, i] = new_pix[img.width-2,i]
        


    return new_img

def main():
    # img = abrir_imagem("8x8.png")
    img = abrir_imagem("BolsoSimpson.jpg")
    img = escala_de_cinza(img)
    img.show()
    # print(matriz_da_imagem(img))
    print('----------------------------')
    img = filtro_media(img)
    # print(matriz_da_imagem(img))
    img.show()
    

    

if __name__ == '__main__':
    main()
    
    
