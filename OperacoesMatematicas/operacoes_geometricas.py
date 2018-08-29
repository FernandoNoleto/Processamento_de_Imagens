'''
UNIVERSIDADE FEDERAL DO TOCANTINS
TRABALHO DE PROCESSAMENTO DE IMAGENS
ACADÊMICOS: FERNANDO NOLETO E THIAGO SILVA
AGOSTO DE 2018
'''

from PIL import Image, ImageFilter
import numpy as np
import sys
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


#Função que realiza a translação
#Parâmetros: novo x e novo y -> para onde a imagem vai ser transladada
def translacao(image,new_x,new_y):
    size = image.size
    size = size[0] + abs(new_x) , size[1] + abs(new_y)
    new = Image.new("L",(size))
    # X positive Y Positive
    if new_x >= 0 and new_y >= 0:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i+new_x,j), image.getpixel(p)) 
        return new
    # X negative , Y negative
    if new_x < 0 and new_y < 0:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i,j+ abs(new_y)), image.getpixel(p)) 
        return new
    # X negative, Y positive
    if new_x < 0 and new_y > 0: 
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i,j), image.getpixel(p)) 
        return new  
    # X positive , Y negative
    else:
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                p = (i,j)
                new.putpixel((i + abs(new_x), j + abs(new_y)), image.getpixel(p)) 
        return new  
        
#Função que realiza a reflexão
#Parâmentro: eixo -> em qual eixo vai ser feito a reflexão
def reflexao(image, eixo):    
    x = lambda x: x
    y = lambda y: y    
    
    if "x" in eixo:
        x = lambda x: image.size[0] -1 -x
    elif "y" in eixo: 
        y = lambda y: image.size[1] -1 -y

    new_image = Image.new("L", image.size)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            new_image.putpixel( (x(i), y(j) ), image.getpixel( (i,j) ) )

    return new_image

    
def main():
    #gumball-rapper.jpg
    # img = abrir_imagem('gumball-rapper.jpg')
    # img = converter_para_escala_de_cinza(img)
    # img.show()

    # rotacao(img, 90)

    if len(sys.argv) < 2:
        print("utilize o comando 'python operacoes_geometricas.py 'imagem' 't|r' ")
        exit()
    else :
        if sys.argv[2] == 't' :           
            if len(sys.argv) < 5:
                print("utilize o comando 'python operacoes_geometricas.py 'imagem' 'opcao' 'X Y' ")
                exit()
            else:
                opt = int(sys.argv[3])
                opt1 = int(sys.argv[4])
                translacao(Image.open(sys.argv[1]).convert("L"), opt, opt1).show()
        elif sys.argv[2] == 'r' :
            if len(sys.argv) < 4:
                print("utilize o comando 'python operacoes_geometricas.py 'imagem' 'opcao' 'X ou Y' ")
                exit()
            else :
                reflexao(Image.open(sys.argv[1]).convert("L"), sys.argv[3]).show()
    
    

if __name__ == '__main__':
    main()