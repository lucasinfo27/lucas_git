global digite

idosos = []
gestantes = []
comuns = []

print("|", idosos,   "|")
print("|", gestantes,"|")
print("|", comuns,   "|")

digite = ''
while digite != '0':
    print()
    digite = str(input("Se voce quer entrar na fila digite 'sim', se voce quer remover alguem da fila digite 'retirar' digite 0 para terminar a operancao .---> "))
    print()
    if digite == 'sim':
        print()
        n1 = input("digite 1 se voce for idoso, digite 2 se voce for gestante, digite 3 se voce for uma pessoa comum: ")
        nome = input('digite seu nome')
        print()

        if n1 == '1':
            idosos.append(nome)
        elif n1 == '2':
            gestantes.append(nome)
        elif n1 == '3':
            comuns.append(nome)

    elif digite == 'retirar':
        if len(idosos) > 0:
            print(idosos[0],'Foi atendido(a)')
            del(idosos[0])
        else:
            if len(gestantes) > 0:
                print(gestantes[0],'Foi atendida')
                del(gestantes[0])
            else:
                if len(comuns) > 0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                    print(comuns[0],'Foi atendido(a)')
                    del(comuns[0])
                else:
                    print('As Filas estão vazias!')
    print()
    print(idosos)
    print(gestantes)
    print(comuns)
    print()

    if digite == '0':
        print("Fechando o programa ate logo")
             
    
    







   
