'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
AGOSTO DE 2018
'''

from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from itertools import product
import math, random


class Rotulos(object):

    # letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    # rot = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, rotulo, x, y):
        self.rotulo = rotulo
        self.x = x
        self.y = y

#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

#Converte a imagem para preto e branco
def binarizar_imagem(img):
    return img.convert('L')

def gerar_matriz (n_linhas, n_colunas):
    matriz = np.zeros((n_linhas, n_colunas), dtype=np.str)
    return matriz

def imprimir_matriz(matriz):
    print(np.asarray(matriz))

#Decobrir se as posicoes passadas como paramentro possuem o mesmo rotulo
def mesmo_label(tabela_de_rotulacao, x, y, i, j):
    for aux1 in tabela_de_rotulacao:
        if aux1.x == x and aux1.y == y:
            break
    for aux2 in tabela_de_rotulacao:
        if aux2.x == i and aux2.y == j:
            break
    
    if aux1.rotulo == aux2.rotulo:
        # print('aux1.rotulo: {}'.format(aux1.rotulo))
        # print('aux2.rotulo: {}'.format(aux2.rotulo))
        return True
    else: 
        return False

#Decobrir qual o rotulo de uma determinada posicao
def descobrir_rotulo(tabela_de_rotulacao, x, y):
    for aux in tabela_de_rotulacao:
        if aux.x == x and aux.y == y:
            return aux.rotulo
    
    return "X"

def uniao(tabela_de_rotulacao, label1, label2):
    for aux in tabela_de_rotulacao:
        if aux.rotulo == label2:
            aux.rotulo = label1
    return tabela_de_rotulacao

def preencher_tabela(tabela_de_rotulacao, matriz):
    
    for r in tabela_de_rotulacao:
        matriz[r.y, r.x] = r.rotulo
    
    return matriz

def rotulacao(img):
    pix = img.load()

    # print(np.asarray(img.convert('L')))
    # rotulacao = Tabela_de_rotulacao()

    preto = 0
    branco = 255
    
    rotulo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    tabela_de_rotulacao = []

    width, height = img.size
    matriz = gerar_matriz(img.height, img.width)
 
    for y, x in product(range(height), range(width)):

        #se for branco nao faz nada
        #if pix[x,y] == 255:
        #    pass
        
        #se for preto
        if pix[x,y] == preto:
            #a partir da posicao 1,1
            if x > 0 and y > 0:
                #2.1 - Se r e s forem branco, assinala-se um novo label para p e
                #anota-se que esse label já foi usado
                if pix[x-1,y] == branco and pix[x,y-1] == branco:
                    novo_rotulo = Rotulos(rotulo[count], x, y)
                    count += 1
                    tabela_de_rotulacao.append(novo_rotulo)
                
                #2.2- Se r ou s for preto, assinala-se label correspondente a p
                #pixel da esquerda
                elif pix[x-1,y] == preto:
                    for aux in tabela_de_rotulacao:
                        if aux.x == x-1:
                            novo_rotulo = Rotulos(aux.rotulo, x, y)
                            tabela_de_rotulacao.append(novo_rotulo)
                #pixel acima
                elif pix[x,y-1] == preto:
                    for aux in tabela_de_rotulacao:
                        if aux.y == y-1:
                            novo_rotulo = Rotulos(aux.rotulo, x, y)
                            tabela_de_rotulacao.append(novo_rotulo)
                
                #2.3- Se r e s forem preto
                elif pix[x-1,y] == preto and pix[x,y-1] == preto:
                    #for aux in tabela_de_rotulacao:
                    #tem o mesmo label
                    if mesmo_label(tabela_de_rotulacao, x-1, y, x, y-1):
                        # print(descobrir_rotulo(tabela_de_rotulacao, x, y-1))
                        novo_rotulo = Rotulos(descobrir_rotulo(tabela_de_rotulacao, x, y-1), x, y)
                    #nao tem o mesmo label
                    else:
                        novo_rotulo = Rotulos(descobrir_rotulo(tabela_de_rotulacao, x-1, y), x, y)
                        tabela_de_rotulacao = uniao(tabela_de_rotulacao, descobrir_rotulo(tabela_de_rotulacao, x-1, y), descobrir_rotulo(tabela_de_rotulacao, x, y-1))
                        count -= 1

            #se for a posicao 0,0:
            elif x == 0 and y == 0:
                if pix[x,y] == preto:
                    novo_rotulo = Rotulos(rotulo[count], x, y)
                    tabela_de_rotulacao.append(novo_rotulo)

            # Se for na 1 linha
            elif y == 0 and x >= 1:
                if pix[x-1, y] == preto:
                    novo_rotulo = Rotulos(descobrir_rotulo(tabela_de_rotulacao, x-1, y), x, y)
                    tabela_de_rotulacao.append(novo_rotulo)
                else:
                    novo_rotulo = Rotulos(rotulo[count], x, y)
                    count +=1
                    tabela_de_rotulacao.append(novo_rotulo)
            
            # Se for na 1 coluna
            elif x == 0 and y >= 1:
                if pix[x, y-1] == preto:
                    novo_rotulo = Rotulos(descobrir_rotulo(tabela_de_rotulacao, x, y-1), x, y)
                    tabela_de_rotulacao.append(novo_rotulo)
                else:
                    novo_rotulo = Rotulos(rotulo[count], x, y)
                    count +=1
                    tabela_de_rotulacao.append(novo_rotulo)
        
    #endfor

    

    for r in tabela_de_rotulacao:
        matriz[r.y, r.x] = r.rotulo
    
    imprimir_matriz(matriz)

    print('Labels encontradas: {}'.format(count))

    return tabela_de_rotulacao

def colorir_imagem(img, tabela_de_rotulacao):
    width, height = img.size
    img_colorida = Image.new("RGB", (width, height))
    pix = img_colorida.load()

    # cores = Cores()
    rotulo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    nova_cor = {}
    for aux in tabela_de_rotulacao:
        if aux.rotulo not in nova_cor:
            nova_cor[rotulo[count]] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            count += 1
        

    # for k,v in nova_cor.items():
    #     print('k: {}, v: {}'.format(k,v))
    
    
    for aux in tabela_de_rotulacao:
        for k,v in nova_cor.items():
            if aux.rotulo == k:
                pix[aux.x, aux.y] = v
        
            


    
    img_colorida.save('imagem_rotulada.png')
    return img_colorida


# 0 = preto
# 1 = 255 = branco
# classificar o que for preto


def main():
    img = abrir_imagem("black_white.png")
    img = binarizar_imagem(img)
    #img.save('binarized_img.png')

    # tabela_de_rotulacao = rotulacao(img)

    colorir_imagem(img, rotulacao(img))



if __name__ == '__main__':
    main()