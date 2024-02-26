import numpy as np
matriz = np.array([[2,3,1], #matriz de 2 linhas e 3 colunas
                   [4,5,7]])
#print(matriz) #traz a matriz conforme foi declarada (tipo acima)
#print (matriz.shape) devolve a qtd de linhas/colunas da matriz
#print (matriz[0]) devolve o que está na linha 0
#print (matriz[0][0]) devolve o que está na coluna 0 na linha 0

#percorrendo matriz
for i in range(matriz.shape[0]):
    print(matriz[i]) #traz o que está nas linhas da matriz
    for j in range(matriz.shape[1]): #pq o shape retorna linha[0], coluna[1]. 
        print(matriz[i][j])