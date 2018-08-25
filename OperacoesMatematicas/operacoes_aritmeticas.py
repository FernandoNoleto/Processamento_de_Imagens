'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
AGOSTO DE 2018
'''

from PIL import Image, ImageFilter
import numpy as np

#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

#Retorna a imagem em escala de cinza
def converter_para_escala_de_cinza(img):
    return img.convert('L')

#Cria nova imagem toda branca com o mesmo tamanho da imagem original
#para ser preenchida posteriormente
def nova_imagem(img):
    return Image.new('L', (int(img.width), int(img.height)), color = 'white')

#Imprime a matriz da imagem passada como parâmetro
def imprimir_matriz(img):
    print(np.asarray(img.convert('L')))

#Adição de 2 imagens
def adicao(img, img2):
    new_img = nova_imagem(img)
    pix  = img.load()
    pix2 = img2.load()
    pix3 = new_img.load()


    for i in range(img.width):
        for j in range(img.height):
            pix3[i,j] = int(pix[i,j] + pix2[i,j]/2)
    
    new_img.save('adicao.png')
    new_img.show()

    return new_img

#Subtração de 2 imagens
def subtracao(img, img2):
    new_img = nova_imagem(img)
    pix  = img.load()
    pix2 = img2.load()
    pix3 = new_img.load()


    for i in range(img.width):
        for j in range(img.height):
            if int(pix[i,j] - pix2[i,j]/2) < 0: #caso a diferença for < 0
                pix3[i,j] = 0
            else:
                pix3[i,j] = int(pix[i,j] - pix2[i,j]/2)
    
    new_img.save('subtracao.png')
    new_img.show()

    return new_img



def main():
    img  = abrir_imagem('grayscale.jpg')
    img2 = abrir_imagem('grayscale2.jpg') 
    img  = converter_para_escala_de_cinza(img)
    img2 = converter_para_escala_de_cinza(img2)

    adicao(img, img2)
    subtracao(img, img2)
    

if __name__ == '__main__':
    main()