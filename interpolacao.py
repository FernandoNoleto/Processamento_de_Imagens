'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
AGOSTO DE 2018
'''

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
    img = Image.open(nome_img)
    return img


#Converte a imagem original para a escala de cinza
def converter_para_escala_de_cinza(img):
    img = img.convert('L')
    return img


#Cria nova imagem toda branca com a metade do tamanho da imagem original
#para ser preenchida posteriormente
def nova_imagem_reducao(img):
    new_img = Image.new('L', (int(img.width/2), int(img.height/2)), color = 'white')
    # new_img.save('nova_imagem.png')
    # new_img.show()
    return new_img


#Cria nova imagem toda branca com o dobro do tamanho da imagem original
#para ser preenchida posteriormente
def nova_imagem_ampliacao(img):
    new_img = Image.new('L', (img.width*2, img.height*2), color = 'black')
    # new_img.save('nova_imagem.png')
    # new_img.show()
    return new_img


#Imprime a matriz da imagem passada como parâmetro
def imprimir_matriz(img):
    print(np.asarray(img.convert('L')))


#Passa a imagem original como parametro
#Retorna a nova imagem reduzida preenchida com novos valores
def interpolacao_vizinho_mais_proximo_reducao(img):
    new_img = nova_imagem_reducao(img)
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
    

    new_img.save('imagem_reduzida_vizinho_mais_proximo.png')
    return new_img


#Passa a imagem original como parametro
#Retorna a nova imagem ampliada preenchida com novos valores
def interpolacao_vizinho_mais_proximo_ampliacao(img):
    new_img = nova_imagem_ampliacao(img)
    pix = new_img.load()
    pix2 = img.load()

    k = 0
    l = 0

    for i in range(0, new_img.height, 2):
        for j in range(0, new_img.width, 2):
            pix[i,j] = pix2[k,l]
            if(j < new_img.width):
                pix[i, j+1] = pix2[k,l]
            if(i < new_img.height):
                pix[i+1, j] = pix2[k,l]
            if(i < new_img.height and j < new_img.width):
                pix[i+1, j+1] = pix2[k,l]
            l+=1
        l=0
        k+=1
    
    new_img.save('imagem_ampliada_vizinho_mais_proximo.png')
    return new_img


#Passa a imagem original como parametro
#Retorna a nova imagem reduzida preenchida com novos valores
def interpolacao_bilinear_reducao(img):
    new_img = nova_imagem_reducao(img)
    pix = new_img.load()
    pix2 = img.load()

    k = 0
    l = 0

    for i in range(0, img.height, 2):
        for j in range(0, img.width, 2):
            pix[k,l] = int((pix2[i,j] + pix2[i,j+1] + pix2[i+1,j] + pix2[i+1,j+1]) / 4)
            l+=1
        l=0
        k+=1
    
    new_img.save('imagem_reduzida_bilinear.png')
    return new_img


#Passa a imagem original como parametro
#Retorna a nova imagem ampliada preenchida com novos valores
def interpolacao_bilinear_ampliacao(img):
    new_img = nova_imagem_ampliacao(img)
    pix2 = new_img.load()
    pix = img.load()
    
    
    k = 1#coluna
    l = 0#linha

    #pix2 = nova imagem
    #pix = imagem original

    for i in range(img.height):
        for j in range(img.width):
            pix2[i*2,j*2] = pix[i,j]
            
    # i = 0
    # j = 0
    #preenchimento por linha
    for i in range(img.height):
        for j in range(img.width -1):
            pix2[k,l] = int((pix[j, i] + pix[j+1, i]) / 2)
            k+=2
        k = 1
        l+=2
    
    k = 0#coluna
    l = 1#linha

    #preenchimento por coluna
    for i in range(img.height -1):
        for j in range(img.width):
            pix2[k,l] = int((pix[j, i] + pix[j, i+1]) / 2)
            k+=2
        k = 0
        l+=2

    k = 1
    l = 1

    #preenchimento diagonal
    for i in range(img.height -1):
        for j in range(img.width -1):
            pix2[k,l] = int((pix[j, i] + pix[j, i+1] + pix[j+1,i] + pix[j+1,i+1]) / 4)
            k+=2
        k = 1
        l+=2
    
    #duplicar ultima linha
    for i in range(new_img.width):
        pix2[i, new_img.height -1] = pix2[i, new_img.height -2]
    
    #duplicar ultima coluna
    for i in range(new_img.height):
        pix2[new_img.width -1, i] = pix2[new_img.width -2, i]
    

    # print(np.asarray(img.convert('L')))
    # print(np.asarray(new_img.convert('L')))


    new_img.save('imagem_ampliada_bilinear.png')
    return new_img


def main(opc):

    if opc > 4 or opc < 1:
        print('Opção inválida!')
        return
    
    img = abrir_imagem('BolsoSimpson.jpg')
    # img = abrir_imagem('4x4.png')
    img.show()
    img = converter_para_escala_de_cinza(img)
    
    #vizinho mais proximo reducao
    if opc == 1:
        new_img = interpolacao_vizinho_mais_proximo_reducao(img)
        new_img.show()

    #vizinho mais proximo ampliacao
    elif opc == 2:
        new_img = interpolacao_vizinho_mais_proximo_ampliacao(img)
        new_img.show()

    #bilinear reducao
    elif opc == 3:
        new_img = interpolacao_bilinear_reducao(img)
        new_img.show()

    #bilinear ampliacao
    elif opc == 4:
        new_img = interpolacao_bilinear_ampliacao(img)
        new_img.show()
    
    # else:
    #     print('Escolha inválida!')
    # imprimir_matriz(new_img)
    

if __name__ == '__main__':
    print('1 - Interpolação vizinho mais próximo redução')
    print('2 - Interpolação vizinho mais próximo ampliação')
    print('3 - Interpolação bilinear redução')
    print('4 - Interpolação bilinear ampliação')
    opc = int(input('Escolha uma opção:. '))
    main(opc)