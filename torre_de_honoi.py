import sys

jogadas = 0
coluna1 = []
coluna2 = []
coluna3 = []
hasteInicial = []
verifica = True

def verificacao(de_Qual, para_Qual, jogadas):
    if len(de_Qual) == 0:
        print("MOVIMENTO INVÁLIDO")
        jogadas = jogadas
    elif len(de_Qual) != 0:
        if len(para_Qual) == 0:
            para_Qual.append(de_Qual[-1])
            del(de_Qual[-1])
            jogadas = jogadas + 1
            print("Ja foram %s jogada(s)" % jogadas)
        elif len(pQual) != 0:
            if para_Qual[-1] < de_Qual[-1]:
                print("MOVIMENTO INVÁLIDO!")
            else:
                para_Qual.append(dQual[-1])
                del(de_Qual[-1])
                jogadas = jogadas + 1
                print("Ja foram %s jogada(s)" % jogadas)
        
def ganhador():
    global verifica, coluna1, coluna2, coluna3, nPecas, jogadas, hasteInicial
    if coluna3 == hasteInicial:
        print('Parabéns você ganhou')
        verifica = input("Desejas jogar novamente? (Y/N): ").upper()
        if verifica == 'Y':
            coluna1 = []
            coluna2 = []
            coluna3 = []
            hasteInicial = []
            jogadas = 0
            nPecas = int(input("Número de peças: "))
            print('Seu número mínimo de jogadas é',2**nPecas-1)
            for i in range(nPecas, 0, -1):
                coluna1.append(i)
                hasteInicial.append(i)
        
            print()
            print("coluna 1:", coluna1)
            print("coluna 2:", coluna2)
            print("coluna 3:", coluna3)
            print()
            verifica = True
        elif verifica == 'N':
            print('Obrigado por jogar!!!')
            verifica = False
            sys.exit()
        
def torre(dQual, pQual, coluna1, coluna2, coluna3):
    verificacao(dQual, pQual, jogadas)
    print()
    print("coluna 1:", coluna1)
    print("coluna 2:", coluna2)
    print("coluna 3:", coluna3)
    print()
    ganhador()

while verifica == True:
    nPecas = int(input("Número de peças: "))
    print('Seu número mínimo de jogadas é',2**nPecas-1)
    for i in range(nPecas, 0, -1):
        coluna1.append(i)
        hasteInicial.append(i)
        
    print()
    print("coluna 1:", coluna1)
    print("coluna 2:", coluna2)
    print("coluna 3:", coluna3)
    print()

    while coluna3 != range(nPecas, 0, -1):
        de_Qual = int(input("De qual coluna você deseja mover: "))
        while de_Qual != 1 and de_Qual != 2 and de_Qual != 3:
            de_Qual = int(input("DADO INVÁLIDO! De qual coluna você deseja mover: "))
        else:
            if de_Qual == 1:
                de_Qual = coluna1
            elif de_Qual == 2:
                de_Qual = coluna2
            elif de_Qual == 3:
                de_Qual = coluna3    
        para_Qual = int(input("Para qual coluna você deseja mover: "))
        while para_Qual != 1 and para_Qual != 2 and para_Qual != 3:
            para_Qual = int(input("DADO INVÁLIDO! De qual coluna você deseja mover: "))
        else:
            if para_Qual == 1:
                para_Qual = coluna1
            elif para_Qual == 2:
                para_Qual = coluna2
            elif para_Qual == 3:
                para_Qual = coluna3
        
        torre(de_Qual, para_Qual, coluna1, coluna2, coluna3)
