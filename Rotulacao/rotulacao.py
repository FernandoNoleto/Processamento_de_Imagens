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
    matriz = np.asarray(img.convert('L'))

    # tabela = Tabela_de_rotulacao()
    rotulos = "ABCDEFGHIJLMNOPQRSTUVXZ" 

    label = 0

    #Dimensões
    altura = np.size(matriz, 0)
    largura = np.size(matriz, 1)

    #Cria matriz de zeros com dimensões de imagem
    matrizAux = np.zeros([altura,largura])

    #Varredura da matriz da imagem e seta 1 ou 0 se o pixel for menor que 127
    for i in range(altura):
        for j in range(largura):
            if matriz[i][j] < 127:
                matrizAux[i][j] = 1
            else:
                matrizAux[i][j] = 0


    #Cria uma matriz de char para usar na rotulação            
    matrizString = np.chararray((altura, largura),unicode=True)
    for i in range(altura):
        for j in range(largura):
            matrizString[i][j] = str(matrizAux[i][j])


    '''
    Aqui vai toda a lógica:

    1ºCaso: Sempre a posição [0][0] da matriz se for 1 vai o primeiro Label
    2ºCaso: Se for o pixel for igual a 1 e  uando o i for igual a zero não precisamos checar o pixel de cima ou seja olhamos só o pixel do lado
    3ºCaso: Se for o pixel for igual a 1 e quando o j = 0 não precisamos verificar o pixel do lado pois está no inicio da primeira coluna
    4ºCaso: O restando do caso verifica se for 1 o pixel do lado e o de cima dele se for pelo menos 1 igual repete o label
    '''
    for i in range(altura):
        for j in range(largura):
            #p = self.matriz[i][j]
            r = j-1
            t = i-1
            
            if i == 0 and j == 0: #primeira linha, primeria coluna
                if matrizAux[i][j] == 1:
                    matrizString[i][j] = rotulos[label]
                    label += 1
            elif i == 0 and matrizAux[i][j] == 1: # primeira linha, preto
                if matrizAux[i][r] == 1:
                    matrizString[i][j] = rotulos[label-1]
                else:
                    matrizString[i][j] = rotulos[label]
                    label += 1
            elif matrizAux[i][j] == 1: #linha > 0, preto
                if j == 0:
                    if matrizAux[t][j] == 1:
                        matrizString[i][j] = rotulos[label-1]
                    else:
                        matrizString[i][j] = rotulos[label]
                        label += 1
                elif matrizAux[t][j] == 1 or matrizAux[i][r] == 1:
                    matrizString[i][j] = rotulos[label-1]
                else:
                    matrizString[i][j] = rotulos[label]
                    label += 1

    print(matrizString)
def main():
    img = abrir_imagem("black_white.png")
    #img = binarizar_imagem(img)
    #img.save('binarized_img.png')

    rotulacao(img)



if __name__ == '__main__':
    main()