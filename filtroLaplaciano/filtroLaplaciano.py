'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
SETEMBRO DE 2018
'''

from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

#Abre uma imagem
def abrir_imagem(nome_img):
    return Image.open(nome_img)

def imprimir_matriz(matriz):
    print(np.asarray(matriz))

def matriz_da_imagem(img):
    return np.asarray(img.convert('L'))

def escala_de_cinza(img):
    return img.convert('L')

def menu():
    opc = input('Qual o filtro? A | B | C | D | E | F -> E e F são filtros de Sobel: ')
    # print (opc)
    # print (type(opc))
    return opc

def filtroLaplaciano(img, opc):
    # opc = menu()
    
    #filtro laplaciano
    filtroA = [-1,-1,-1,-1,8,-1,-1,-1,-1]
    filtroB = [1,1,1,1,-8,1,1,1,1]
    filtroC = [0,-1,0,-1,4,-1,0,-1,0]
    filtroD = [0,1,0,1,-4,1,0,1,0]
    #Filtro de sobel
    filtroE = [-1,-2,-1,0,0,0,1,2,1]
    filtroF = [-1,0,1,-2,0,2,-1,0,1]
    
    new_img = Image.new('L', (img.width, img.height), color = 'black')
    pix = img.load()
    new_pix = new_img.load()
    
    #Se o for o filtro A
    if opc == 'a' or opc == 'A':
        for i in range(img.height - 2):
            for j in range(img.width - 2):
                valor = int((pix[i,j]     * filtroA[0] +
                            pix[i,j+1]   * filtroA[1] +
                            pix[i,j+2]   * filtroA[2] +
                            pix[i+1,j]   * filtroA[3] +
                            pix[i+1,j+1] * filtroA[4] +
                            pix[i+1,j+2] * filtroA[5] +
                            pix[i+2,j]   * filtroA[6] +
                            pix[i+2,j+1] * filtroA[7] +
                            pix[i+2,j+2] * filtroA[8]) /9)
                if valor < 0:
                    new_pix[i+1,j+1] = 0
                elif valor > 255:
                    new_pix[i+1,j+1] = 255
                else:
                    new_pix[i+1,j+1] = valor
    
    #Se o for o filtro B
    elif opc == 'b' or opc == 'B':
        for i in range(img.height - 2):
            for j in range(img.width - 2):
                valor = int((pix[i,j]    * filtroB[0] +
                            pix[i,j+1]   * filtroB[1] +
                            pix[i,j+2]   * filtroB[2] +
                            pix[i+1,j]   * filtroB[3] +
                            pix[i+1,j+1] * filtroB[4] +
                            pix[i+1,j+2] * filtroB[5] +
                            pix[i+2,j]   * filtroB[6] +
                            pix[i+2,j+1] * filtroB[7] +
                            pix[i+2,j+2] * filtroB[8]) /9)
                if valor < 0:
                    new_pix[i+1,j+1] = 0
                elif valor > 255:
                    new_pix[i+1,j+1] = 255
                else:
                    new_pix[i+1,j+1] = valor

    #Se o for o filtro C
    elif opc == 'c' or opc == 'C':
        for i in range(img.height - 2):
            for j in range(img.width - 2):
                valor = int((pix[i,j]    * filtroC[0] +
                            pix[i,j+1]   * filtroC[1] +
                            pix[i,j+2]   * filtroC[2] +
                            pix[i+1,j]   * filtroC[3] +
                            pix[i+1,j+1] * filtroC[4] +
                            pix[i+1,j+2] * filtroC[5] +
                            pix[i+2,j]   * filtroC[6] +
                            pix[i+2,j+1] * filtroC[7] +
                            pix[i+2,j+2] * filtroC[8]) /9)
                if valor < 0:
                    new_pix[i+1,j+1] = 0
                elif valor > 255:
                    new_pix[i+1,j+1] = 255
                else:
                    new_pix[i+1,j+1] = valor
    
    #Se o for o filtro D
    elif opc == 'd' or opc == 'D':
        for i in range(img.height - 2):
            for j in range(img.width - 2):
                valor = int((pix[i,j]    * filtroD[0] +
                            pix[i,j+1]   * filtroD[1] +
                            pix[i,j+2]   * filtroD[2] +
                            pix[i+1,j]   * filtroD[3] +
                            pix[i+1,j+1] * filtroD[4] +
                            pix[i+1,j+2] * filtroD[5] +
                            pix[i+2,j]   * filtroD[6] +
                            pix[i+2,j+1] * filtroD[7] +
                            pix[i+2,j+2] * filtroD[8]) /9)
                if valor < 0:
                    new_pix[i+1,j+1] = 0
                elif valor > 255:
                    new_pix[i+1,j+1] = 255
                else:
                    new_pix[i+1,j+1] = valor
    
    #Se o for o filtro E
    elif opc == 'e' or opc == 'E':
        for i in range(img.height - 2):
            for j in range(img.width - 2):
                valor = int((pix[i,j]    * filtroE[0] +
                            pix[i,j+1]   * filtroE[1] +
                            pix[i,j+2]   * filtroE[2] +
                            pix[i+1,j]   * filtroE[3] +
                            pix[i+1,j+1] * filtroE[4] +
                            pix[i+1,j+2] * filtroE[5] +
                            pix[i+2,j]   * filtroE[6] +
                            pix[i+2,j+1] * filtroE[7] +
                            pix[i+2,j+2] * filtroE[8]) /9)
                if valor < 0:
                    new_pix[i+1,j+1] = 0
                elif valor > 255:
                    new_pix[i+1,j+1] = 255
                else:
                    new_pix[i+1,j+1] = valor
    
    #Se o for o filtro F
    elif opc == 'f' or opc == 'F':
        for i in range(img.height - 2):
            for j in range(img.width - 2):
                valor = int((pix[i,j]    * filtroF[0] +
                            pix[i,j+1]   * filtroF[1] +
                            pix[i,j+2]   * filtroF[2] +
                            pix[i+1,j]   * filtroF[3] +
                            pix[i+1,j+1] * filtroF[4] +
                            pix[i+1,j+2] * filtroF[5] +
                            pix[i+2,j]   * filtroF[6] +
                            pix[i+2,j+1] * filtroF[7] +
                            pix[i+2,j+2] * filtroF[8]) /9)
                if valor < 0:
                    new_pix[i+1,j+1] = 0
                elif valor > 255:
                    new_pix[i+1,j+1] = 255
                else:
                    new_pix[i+1,j+1] = valor

    
    for i in range(img.height):
        for j in range(img.width):
            if(i == 0):
                new_pix[i,j] = pix[i,j]
            if(j == 0 and i > 0):
                new_pix[i,j] = pix[i,j]
            if(i == img.height):
                new_pix[i,j] = pix[i,j]
            if(j == img.width):
                new_pix[i,j] = pix[i,j]
    
    return new_img
                    


def main():
    img = abrir_imagem("BolsoSimpson.jpg")
    img = escala_de_cinza(img)
    opc = menu()
    img.show()
    img = filtroLaplaciano(img, opc)
    img.show()
    
        
if __name__ == '__main__':
    main()