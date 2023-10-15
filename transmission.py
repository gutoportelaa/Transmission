#matriz dada na questão
matriz = [[0,1,1,1,1], 
          [1,0,1,1,0], 
          [0,1,0,1,0], 
          [0,0,1,0,1], 
          [0,0,0,1,0]]


#Multiplica as matrizes(matriz1 e matriz2) e retorna a matriz resultante(matriz3)
#a qauntidade de linhas(m) da matriz resultante é igual a quant_transmissoesidade de linhas da matriz1
#a quant_transmissoesidade de colunas(p) da matriz resultante é igual a quant_transmissoesidade de colunas da matriz2
#o numero de colunas da matriz1 deve ser igual ao numero de linhas da matriz2(n)

def multiplicarMatriz(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("Nao e possivel multiplicar as matrizes")
        return
    matriz3 = []
    m = len(matriz1)
    n = len(matriz2)
    p = len(matriz2[0])
    for i in range(m):
        matriz3.append([])
        for j in range(p):
            matriz3[i].append(0)
            for k in range(n):
                matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
    return matriz3


#Retorna a quantidade total de transmissoes possiveis (quant_transmissoes) entre a estacao inicial e a estacao final
#A quantidade de retransmissoes é a quantidade de vezes que a matriz é multiplicada por ela mesma
#A matriz auxiliar(matriz_aux) é inicializada com a matriz dada na questao
#a quant_transmissoes é inicializda com a quantidade de transmissoes diretas entre a estacao inicial e a estacao final
#apos a multiplicação da matriz auxiliar pela matriz dada na questao, a quant_transmissoes é atualizada com a quantidade de transmissoes entre a estacao inicial e a estacao final

def transmissao(matriz, estacao_inicial, estacao_final, quantidade_de_retransmissoes):
    matriz_aux = matriz
    quant_transmissoes = matriz_aux[estacao_inicial][estacao_final]
    for i in range(quantidade_de_retransmissoes):
        matriz_aux = multiplicarMatriz(matriz_aux, matriz)
        quant_transmissoes += matriz_aux[estacao_inicial][estacao_final]
    return quant_transmissoes

#Imprime a quantidade de transmissoes diretas e indiretas entre a estacao inicial e a estacao final
#A matriz auxiliar(matriz_aux) é inicializada com a matriz dada na questao
#do mesmo modo que a função transmissao, a matriz auxiliar é multiplicada pela matriz dada na questao a quantidade de vezes que a quantidade de retransmissoes
#é printada na tela a quantidade de transmissoes diretas e indiretas entre a estacao inicial e a estacao final
#sempre considerando uma posição específica de interesse da matriz auxiliar (matriz_aux[estacao_inicial][estacao_final] == matriz_aux[li][lj])

def printa_quant_transmissoesidade_por_sinal(matriz, estacao_inicial, estacao_final, quantidade_de_retransmissoes):
    print("Diretamente: ", matriz[estacao_inicial][estacao_final])
    matriz_aux = matriz
    for i in range(quantidade_de_retransmissoes):
        matriz_aux = multiplicarMatriz(matriz_aux, matriz)
        print("Com", i+1, "retransmissao: ", matriz_aux[estacao_inicial][estacao_final])

li = 0
lj = 0
while li <= 0 or li > 5:
    try:
        li = int(input("Digite a estacao inicial: "))
        if li <=0 or li > 5:
            print("Valor invalido, so existem 5 estacoes")
    except ValueError:
        print("Valor invalido")
        print("Leva o trabalho dos outros a serio, por favor")
while lj <= 0 or lj > 5:
    try:
        lj = int(input("Digite a estacao final: "))
        if lj <=0 or lj > 5:
            print("Valor invalido, so existem 5 estacoes")
    except ValueError:
        print("Valor invalido")
        print("para com isso irmao")
li-=1
lj-=1
#devemos subtrair 1 das variaveis li e lj pois a matriz em python começa em 0 e não em 1

quantidade_de_retransmissoes = int(input("Digite a quantidade maxima de retransmissoes: "))
total_transmissoes = transmissao(matriz, li, lj, quantidade_de_retransmissoes)
if total_transmissoes > 0:
    print("\nestacao",li+1,"-> estacao",lj+1)
    print("Total de possibilidades de transmissao = ", total_transmissoes)
    printa_quant_transmissoesidade_por_sinal(matriz, li, lj, quantidade_de_retransmissoes)
else:
    print("\nNao ha possibilidade de transmissao entre as estações ", li+1, " e ", lj+1, " com ", quantidade_de_retransmissoes, " retransmissoes")