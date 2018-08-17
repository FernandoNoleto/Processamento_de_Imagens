from PIL import Image, ImageFilter
import numpy as np

def abrir_imagem(nome_img):
    img = Image.open(nome_img) # Can be many different formats.
    return img

def converter_para_escala_de_cinza(img):
    img = img.convert('L') # Convert image to monochrome
    return img

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


def main():
    img = abrir_imagem('BolsoSimpson.jpg')
    pix = img.load()
    x = 1
    y = 1
    # value = 0
    print('size: {}'.format(img.size))  # Get the width and height of the image for iterating over
    print('pix: {}'.format(pix[x,y]))  # Get the RGBA Value of the a pixel of an image


    img = converter_para_escala_de_cinza(img)
    

    # for i in range(0, img.height, 2):
    #     for j in range(0, img.width, 2):
    #         pix[i,j] = 0
            
    # pix[x,y] = value  # Set the RGBA Value of the image (tuple)
    img.save('grayscale.png')  # Save the modified pixels as .png
    # img.show()

    # img = Image.open('grayscale.png')
    # pix = img.load()
    # print('pix: {}'.format(pix[x,y]))

    nova_matriz = interpolacao_vizinho_mais_proximo(img, img.width, img.height)
    print('Matriz reduzida (Vizinho mais proximo): ')
    imprimir_matriz(nova_matriz)

if __name__ == '__main__':
    main()