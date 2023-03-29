'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
ALGORITMOS EM GRAFOS
Filipe Castro Fernandes 2022002088
Atividade 01 -> 29/03/2023
===================================================='''

from igraph import *
import matplotlib.pyplot as plt
import numpy as np

inst = 'ponte.txt' #seleciona o nome da instancia desejada

matrix = np.loadtxt(inst) #copia os dados do .txt para a matriz numpy

plt.imshow(matrix) #plota um mapa da matriz para conferir se os dados 
plt.show()         #foram copiados corretamente
    
with open('result.txt', '+a') as f:  #abre o arquivo como append para adcionar mais dados ao arquivo existente
    lin , col = matrix.shape #da a quantidade de linhas e colunas
    f.writelines(inst + ' ' + str(lin) + ' ' + str(col)) #cria uma linha com o formato  nome_instância qtd_linhas qtd_colunas
    np.savetxt('result.txt', matrix, fmt=' %d') #salva o grafo no arquivo


