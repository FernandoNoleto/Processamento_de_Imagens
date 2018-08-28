from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

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
    return img.convert('1')

def gerar_matriz (n_linhas, n_colunas):
    matriz = np.zeros((n_linhas, n_colunas), dtype=np.str)
    return matriz

def imprimir_matriz(matriz):
    print(np.asarray(matriz))

'''
def rotulacao(img):
    img = binarizar_imagem(img)
    pix = img.load()

    # print(np.asarray(img.convert('L')))
    # rotulacao = Tabela_de_rotulacao()
    
    rotulo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    tabela_de_rotulacao = []

    for i in range(img.height):
        for j in range(img.width):
            #caso a posicao 0,0 seja um novo rotulo
            if i == 0 and j == 0 and pix[0,0] == 0:
                novo_rotulo = Rotulos(rotulo[count], i, j)
                tabela_de_rotulacao.append(novo_rotulo)
                count +=1
            
            #caso esteja na 1 linha e seja um novo rotulo
            elif i == 0 and pix[i,j] == 0:
                novo_rotulo = Rotulos(rotulo[count], i, j)
                tabela_de_rotulacao.append(novo_rotulo)
                count +=1
            
            #caso esteja na 1 coluna e seja um novo rotulo
            elif j == 0 and pix[i,j] == 0:
                novo_rotulo = Rotulos(rotulo[count], i, j)
                tabela_de_rotulacao.append(novo_rotulo)
                count +=1
            
            #caso esteja a partir da posicao 1,1
            elif i > 0 and j > 0 and pix[i,j] == 0:
                #caso a esquerda e acima forem branco, assinala-se um novo rotulo
                if pix[i-1, j] == 255 and pix[i, j-1] == 255:
                    novo_rotulo = Rotulos(rotulo[count], i, j)
                    tabela_de_rotulacao.append(novo_rotulo)
                    count += 1
                
                #caso a esquerda for preto, assinala-se um rotulo correspondente
                elif pix[i, j-1] == 0 and pix[i,j] == 0:
                    for aux in tabela_de_rotulacao:
                        if aux.x == i and aux.y == j-1:
                            novo_rotulo = Rotulos(aux.rotulo, i, j)
                
                #caso acima for preto, assinala-se um rotulo correspondente
                elif pix[i-1, j] == 0 and pix[i,j] == 0:
                    for aux in tabela_de_rotulacao:
                        if aux.x == i-1 and aux.y == j:
                            novo_rotulo = Rotulos(aux.rotulo, i, j)
                
                #caso acima e a esquerda for preto
                # elif pix[i-1, j] == 0 and pix[i,j-1] == 0 and pix[i,j] == 0:
                #     for aux in tabela_de_rotulacao:
                #         if (aux.x == i-1 and aux.y == j) or (aux.x == i and aux.y == j-1):
                #             novo_rotulo = Rotulos(aux.rotulo, i ,j)
    
    matriz = gerar_matriz(img.height, img.width)

    for r in tabela_de_rotulacao:
        matriz[r.x, r.y] = r.rotulo

    # for r in tabela_de_rotulacao:
    #     print('------------')
    #     print('R: {}'.format(r.rotulo))
    #     print('x: {}'.format(r.x))
    #     print('y: {}'.format(r.y))
    
    # matriz = gerar_matriz(img.height, img.width)

    
    print(np.asarray(matriz))

'''

def rotulacao(img):
    img = binarizar_imagem(img)
    pix = img.load()

    # print(np.asarray(img.convert('L')))
    # rotulacao = Tabela_de_rotulacao()
    
    rotulo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    tabela_de_rotulacao = []

    for i in range(img.height):
        for j in range(img.width):
            #caso a posicao 0,0 seja um novo rotulo
            if i == 0 and j == 0 and pix[0,0] == 0:
                novo_rotulo = Rotulos(rotulo[count], j, i)
                tabela_de_rotulacao.append(novo_rotulo)
                count +=1
            
            #caso esteja na 1 linha
            elif i == 0 and pix[i,j] == 0:
                if i-1 != 0:
                    novo_rotulo = Rotulos(rotulo[count], j, i)
                    tabela_de_rotulacao.append(novo_rotulo)
                    count +=1
                else:
                    for aux in tabela_de_rotulacao:
                        if aux.y == i-1 and aux.x == j:
                            novo_rotulo = Rotulos(aux.rotulo, j, i)
            
            #caso esteja na 1 coluna e seja um novo rotulo
            elif j == 0 and pix[i,j] == 0:
                novo_rotulo = Rotulos(rotulo[count], j, i)
                tabela_de_rotulacao.append(novo_rotulo)
                count +=1
            
            #caso esteja a partir da posicao 1,1
            elif i > 0 and j > 0 and pix[i,j] == 0:
                #caso a esquerda e acima forem branco, assinala-se um novo rotulo
                if pix[i-1, j] == 255 and pix[i, j-1] == 255:
                    novo_rotulo = Rotulos(rotulo[count], j, i)
                    tabela_de_rotulacao.append(novo_rotulo)
                    count += 1
                
                #caso a esquerda for preto, assinala-se um rotulo correspondente
                elif pix[i, j-1] == 0 and pix[i,j] == 0:
                    for aux in tabela_de_rotulacao:
                        if aux.x == i and aux.y == j-1:
                            novo_rotulo = Rotulos(aux.rotulo, j, i)
                
                #caso acima for preto, assinala-se um rotulo correspondente
                elif pix[i-1, j] == 0 and pix[i,j] == 0:
                    for aux in tabela_de_rotulacao:
                        if aux.x == i-1 and aux.y == j:
                            novo_rotulo = Rotulos(aux.rotulo, j, i)
                
                #caso acima e a esquerda for preto
                # elif pix[i-1, j] == 0 and pix[i,j-1] == 0 and pix[i,j] == 0:
                #     for aux in tabela_de_rotulacao:
                #         if (aux.x == i-1 and aux.y == j) or (aux.x == i and aux.y == j-1):
                #             novo_rotulo = Rotulos(aux.rotulo, i ,j)
    
    matriz = gerar_matriz(img.height, img.width)

    for r in tabela_de_rotulacao:
        matriz[r.x, r.y] = r.rotulo

    # for r in tabela_de_rotulacao:
    #     print('------------')
    #     print('R: {}'.format(r.rotulo))
    #     print('x: {}'.format(r.x))
    #     print('y: {}'.format(r.y))
    
    # matriz = gerar_matriz(img.height, img.width)

    
    print(np.asarray(matriz))



    

                




                


# 0 = preto
# 1 = 255 = branco
# classificar o que for preto


def main():
    img = abrir_imagem("black_white.png")
    #img = binarizar_imagem(img)
    #img.save('binarized_img.png')

    rotulacao(img)



if __name__ == '__main__':
    main()