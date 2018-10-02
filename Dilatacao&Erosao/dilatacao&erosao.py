'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
AGOSTO DE 2018
'''

from PIL import Image, ImageFilter
import numpy as np
from itertools import product
import sys

class Pixel(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Abre uma imagem
def abrir_imagem(nome_img):
    img = Image.open(nome_img)
    return img

def converter_para_escala_de_cinza(img):     
    return img.convert('L')

def binarizar_imagem(img):
    img = converter_para_escala_de_cinza(img)
    pix = img.load()
    
    for i in range(img.width):
        for j in range(img.height):
            if pix[i,j] >= 100:
                pix[i,j] = 255
            else:
                pix[i,j] = 0
    return img
    


#Imprime a matriz da imagem passada como parâmetro
def imprimir_matriz(img):
    print(np.asarray(img.convert('L')))


def dilatacao(img):
    pix = img.load()

    pixels_to_paint = []
    
    width, height = img.size
    for j, i in product(range(height-1), range(width-1)):
        if i > 0 and j > 0:
            if pix[i,j] == 255:
                pixels_to_paint.append(Pixel(i,j))
                # pix[i-1,j] = 255
                # pix[i+1,j] = 255
                # pix[i,j-1] = 255
                # pix[i,j+1] = 255
                # pix[i-1,j-1] = 255
                # pix[i+1,j+1] = 255
                # pix[i-1,j+1] = 255
                # pix[i+1,j-1] = 255
    
    print(pixels_to_paint.__len__())

    for k in pixels_to_paint:
        # print('x: {} y: {}'.format(pixels_to_paint.pop().x, pixels_to_paint.pop().y))
        
        # coluna linha
        pix[pixels_to_paint.pop().x-1, pixels_to_paint.pop().y] = 255 #esquerda
        pix[pixels_to_paint.pop().x+1, pixels_to_paint.pop().y] = 255 #direita
        pix[pixels_to_paint.pop().x, pixels_to_paint.pop().y-1] = 255 #em cima
        pix[pixels_to_paint.pop().x, pixels_to_paint.pop().y+1] = 255 #em baixo
        
        pix[pixels_to_paint.pop().x-1, pixels_to_paint.pop().y-1] = 255 #em cima e esquerda
        pix[pixels_to_paint.pop().x+1, pixels_to_paint.pop().y+1] = 255 #em baixo e direita
        pix[pixels_to_paint.pop().x-1, pixels_to_paint.pop().y+1] = 255 #em baixo e esquerda
        pix[pixels_to_paint.pop().x+1, pixels_to_paint.pop().y-1] = 255 #em cima e direita


    return img

def erosao(img):
    pix = img.load()

    pixels_to_paint = []
    
    width, height = img.size
    for j, i in product(range(height-1), range(width-1)):
        if i > 0 and j > 0:
            if pix[i,j] == 255:
                pixels_to_paint.append(Pixel(i,j))

    
    print(pixels_to_paint.__len__())

    for k in pixels_to_paint:
        # print('x: {} y: {}'.format(pixels_to_paint.pop().x, pixels_to_paint.pop().y))
        
        # coluna linha
        pix[pixels_to_paint.pop().x-1, pixels_to_paint.pop().y] = 0 #esquerda
        pix[pixels_to_paint.pop().x+1, pixels_to_paint.pop().y] = 0 #direita
        pix[pixels_to_paint.pop().x, pixels_to_paint.pop().y-1] = 0 #em cima
        pix[pixels_to_paint.pop().x, pixels_to_paint.pop().y+1] = 0 #em baixo
        
        pix[pixels_to_paint.pop().x-1, pixels_to_paint.pop().y-1] = 0 #em cima e esquerda
        pix[pixels_to_paint.pop().x+1, pixels_to_paint.pop().y+1] = 0 #em baixo e direita
        pix[pixels_to_paint.pop().x-1, pixels_to_paint.pop().y+1] = 0 #em baixo e esquerda
        pix[pixels_to_paint.pop().x+1, pixels_to_paint.pop().y-1] = 0 #em cima e direita




    return img

def main(operacao, nome_da_imagem):
    
    # img = abrir_imagem('word.png')
    # img = abrir_imagem('Google_logo.png')
    # img = abrir_imagem('BolsoSimpson.jpg')

    img = abrir_imagem(nome_da_imagem)
    img = binarizar_imagem(img)
    img.show()

    if operacao == 'dilatacao':
        img = dilatacao(img)
    elif operacao == 'erosao':
        img = erosao(img)
    else:
        print("Algo deu errado!")
    img.show()
    
    
    

if __name__ == '__main__':
    # main()
    if len(sys.argv) < 3 or (sys.argv[1] != 'dilatacao' and sys.argv[1] != 'erosao'):
        print("Execute assim: 'python dilatacao\&erosao.py dilatacao|erosao nomeDaImagem'")
    else:
        main(sys.argv[1], sys.argv[2])