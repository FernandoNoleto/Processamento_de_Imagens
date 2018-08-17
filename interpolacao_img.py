from PIL import Image, ImageFilter
import numpy as np

'''
def interpolacao_vizinho_mais_proximo(img, width, height):
    nova_matriz = []
    x = 0
    y = 0

    for i in range(width/2):
        linha = []
        for j in range(height/2):
            linha.append(img[y][x])
            x += 2
        x = 0
        y += 2
        nova_matriz.append(linha)
    
    return nova_matriz

def imprimir_matriz(matriz):
    print(np.matrix(matriz))
'''

#Abre uma imagem
def abrir_imagem(nome_img):
    img = Image.open(nome_img) # Can be many different formats.
    return img


#Converte a imagem original para a escala de cinza
def converter_para_escala_de_cinza(img):
    img = img.convert('L') # Convert image to monochrome
    return img


#Cria nova imagem toda branca com a metade do tamanho da imagem original
#para ser preenchida posteriormente
def nova_imagem(img):
    new_img = Image.new('L', (img.width/2, img.height/2), color = 'white')
    # new_img.save('nova_imagem.png')
    # new_img.show()
    return new_img


#Passa a imagem original e a nova imagem que ja esta reduzida como parametro
#Retorna a nova imagem preenchida com novos valores
def interpolacao_vizinho_mais_proximo(img, new_img):
    pix = new_img.load()
    pix2 = img.load()

    k = 0
    l = 0
    
    for i in range(0, img.height, 2):
        for j in range(0, img.width, 2):
            pix[k,l] = pix2[i,j]
            l+=1
        l = 0
        k+=1
    

    new_img.save('imagem_reduzida.png')
    return new_img


def main():
    img = abrir_imagem('BolsoSimpson.jpg')
    img.show()
    
    # pix = img.load()
    # x = 1
    # y = 1
    # print('size: {}'.format(img.size))  # Get the width and height of the image for iterating over
    # print('pix: {}'.format(pix[x,y]))  # Get the RGBA Value of the a pixel of an image
    
    
    img = converter_para_escala_de_cinza(img)
    new_img = nova_imagem(img)
    new_img = interpolacao_vizinho_mais_proximo(img, new_img)

    new_img.show()

if __name__ == '__main__':
    main()