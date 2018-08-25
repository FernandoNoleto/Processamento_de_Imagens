'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
AGOSTO DE 2018
'''

from PIL import Image, ImageFilter
import numpy as np
import math

#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

#Retorna a imagem em escala de cinza
def converter_para_escala_de_cinza(img):
    return img.convert('L')

#Cria nova imagem toda branca com o mesmo tamanho da imagem original
#para ser preenchida posteriormente
def nova_imagem(img):

    return (
        Image.new('L', (int(img.width), int(img.width)), color = 'white') if img.width >= img.height
        else Image.new('L', (int(img.height), int(img.height)), color = 'white')
    )

#Imprime a matriz da imagem passada como parâmetro
def imprimir_matriz(img):
    print(np.asarray(img.convert('L')))

def seno(x):
    return int(math.sin(math.radians(x)))

def cosseno(x):
    return int(0 if x == 90 else math.cos(math.radians(x)))

#Rotação
def rotacao(img, theta):
    new_img = nova_imagem(img)
    pix  = img.load()
    pix2 = new_img.load()
    
    # print(new_img.size)

    center = (int(img.width/2), int(img.height/2))
    # print ('centro: {}'.format(center))

    # return

    count = 0

    for h in range(img.height):
        for w in range(img.width):
            # x = int(cosseno(theta) * h -    seno(theta) * w + center[0])
            # y = int(   seno(theta) * h + cosseno(theta) * w + center[1])
            
            x = int( ( ( w * cosseno(theta) ) + (h *    seno(theta) ) ) )
            y = int( ( ( w *    seno(theta) ) - (h * cosseno(theta) ) ) )
            # print('x: {}'.format(x))
            # print('y: {}'.format(y))
            # print('h: {}'.format(h))
            # print('w: {}'.format(w))
            
            pix2[x,y] = pix[w,h]
        
    
    new_img.save('nova_imagem.png')
    new_img.show()
            
    # x2 = math.cos(theta) * (img.width - center[0]) - math.sin(theta) * (img.height - center[1]) + 

def espelhamento(img):
    new_img = nova_imagem(img)
    pix = img.load()
    pix2 = new_img.load()

    for i in range(img.height):
        for j in range(img.width):
            pass


    

def main():
    #gumball-rapper.jpg
    img = abrir_imagem('gumball-rapper.jpg')
    img = converter_para_escala_de_cinza(img)
    # img.show()

    # print(cosseno(90))
    rotacao(img, 90)

    # for i in range(91):
    #     print('{}: {}'.format(i, cosseno(i)))
    
    

if __name__ == '__main__':
    main()