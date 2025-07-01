tipo=0

def partida():
    n = int (input("Quantas peças? "))
    m = int (input("Limite de peças por jogada? "))
    computador = True
    if m > n:
        print("Oops! Jogada inválida! Tente de novo")
        partida()
    if n%(m+1)!=0:
        computador = True
        
    if n%(m+1)==0:
        computador = False
        print ("Voce começa!")
    else:
        print("Computador começa!")
        
    while n > 0:
        if computador:
            jogada = computador_escolhe_jogada(n, m)
            computador = False
            if jogada ==1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", jogada, "peças.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            computador = True
            if jogada == 1:
                print("Você tirou uma peça.")
            else:
                print("voce tirou",jogada,"peças.")
        n = n - jogada
        if n==1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")
    if computador:
        print("Fim de jogo! Você ganhou!")
        return 0
    else:
        print("Fim de jogo! O computador ganhou!")
        return 1

def computador_escolhe_jogada (n,m):  
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m

def usuario_escolhe_jogada(n,m):
    user = int(input("Quantas peças você vai tirar? "))
    if user > m or user < 1 or user > n :
        print("Oops! Jogada inválida! Tente de novo")
        usuario_escolhe_jogada(n,m)
    return user

def campeonato():
    user = 0
    cpu = 0
    partidas = 1
    while partidas < 4:
        print("**** Rodada", partidas ,"****")
        resultado = partida()
        if resultado ==1:
            cpu = cpu + 1
        else:
            user= user + 1
        partidas = partidas + 1
    if user> cpu:
        print("Final do campeonato! Você ganhou!")
        print("Placar: Você",user, "X",cpu," Computador")
    else:
        print("Final do campeonto! O computador ganhou!")
        print("Placar: Você",user, "X",cpu," Computador")
    
while tipo==0:
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    tipo = int (input("2 - para jogar um campeonato "))
    if tipo==1:
        print("Você escolheu uma partida isolada!")
        partida()
        break
    if tipo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
        break
    else:
        tipo = 0
        
