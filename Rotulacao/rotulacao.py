from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

class Tabela_de_rotulacao(object):

    letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

    def __init__(self, rotulo, x, y):
        self.rotulo = rotulo
        self.x = x
        self.y = y


#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

#Converte a imagem para preto e branco
def binarizar_imagem(img):
    return img.convert('1')

#Recebe uma imagem como parâmetro
#Retorna a rotulação da imagem
def rotulacao(img):
    pix = img.load()
    print(np.asarray(img.convert('L')))

    # tabela = Tabela_de_rotulacao()
    tabela = []

    label = 0

    for i in range(img.height):
        for j in range(img.width):
            if pix[j,i] == 0:
                if i > 0 and j > 0:
                    if pix[j-1, i] == 255 and pix[j, i-1] == 255:
                        # pix[j,i] = 
                        novo_label = Tabela_de_rotulacao(label, i, j)
                        label += 1
                        tabela.append(novo_label)
                # elif pix[j-1, i] == 0 and pix[j, i-1] == 0:
    
    # table = tabela.c
    for t in tabela:
        # teste = tabela.pop()
        print('rotulo: {}'.format(t.rotulo))
        print('x: {}'.format(t.x))
        print('y: {}'.format(t.y))

    # d = []
    # d.




def main():
    img = abrir_imagem("black_white.png")
    img = binarizar_imagem(img)
    img.save('binarized_img.png')

    rotulacao(img)



if __name__ == '__main__':
    main()