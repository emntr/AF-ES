import random

# Dicionário de palavras em português
palavras = ["pilha", "fila", "listase", "listasc", "listade", "listadc", "arvore", "bubblesort", "quicksort"]

# Função para criar a árvore binária
def criar_arvore(palavras):
    if not palavras:
        return None

    palavra_pivo = palavras[len(palavras) // 2]
    nodo = {"palavra": palavra_pivo}

    nodo_esquerdo = criar_arvore(palavras[:len(palavras) // 2])
    nodo_direito = criar_arvore(palavras[len(palavras) // 2 + 1:])

    nodo["esquerdo"] = nodo_esquerdo
    nodo["direito"] = nodo_direito

    return nodo

# Função para buscar uma palavra na árvore binária
def buscar_palavra(arvore, letra, palavra_atual):
    if not arvore:
        return None

    palavra_nodo = arvore["palavra"]

    if letra == palavra_nodo[0]:
        if len(palavra_nodo) == 1:
            return palavra_nodo
        else:
            return buscar_palavra(arvore["esquerdo"], letra, palavra_atual + palavra_nodo[0])
    elif letra < palavra_nodo[0]:
        return buscar_palavra(arvore["esquerdo"], letra, palavra_atual)
    else:
        return buscar_palavra(arvore["direito"], letra, palavra_atual)

# Função para jogar
def jogar():
    # Selecionar nível de dificuldade
    dificuldade = int(input("Escolha a dificuldade (1 - Fácil, 2 - Intermediário, 3 - Difícil): "))
    erros_maximos = {1: 10, 2: 7, 3: 5}[dificuldade]

    # Preparar o jogo
    palavra_secreta = random.choice(palavras)
    palavra_atual = ["_" for _ in range(len(palavra_secreta))]
    letras_palpites = []
    pilha_palpites = []
    erros = 0

    # Criar a árvore binária
    arvore = criar_arvore(palavras)

    # Loop principal do jogo
    while True:
        # Exibir o estado do jogo
        print("\nJogo da Forca das estutura de dados !")
        print("\nAs palavras do jogo estao sem espaço, tambem estao em letra minuscula por exemplo: javascript")
        print("\nA palavra lista e suas variaçoes estao abreviadas, por exemplo: lista simples encadeada fica: listase \n")
        print(f"Palavra: {''.join(palavra_atual)}")
        print(f"Tentativas restantes: {erros_maximos - erros}")
        print(f"Letras já usadas: {', '.join(letras_palpites)}")

        # Obter palpite do jogador
        palpite = input("digite uma letra:").lower()

        # Validar palpite
        if palpite == "dica":
            palavra_candidata = buscar_palavra(arvore, palavra_atual[0], "")
            if palavra_candidata:
                print(f"Dica: a palavra pode começar com '{palavra_candidata[0]}'")
            else:
                print("Sem dicas disponíveis no momento.")
            continue

        if not palpite.isalpha() or len(palpite) != 1:
            print("Palpite inválido. Digite apenas uma letra.")
            continue

        if palpite in letras_palpites:
            print("Você já digitou essa letra!")
            continue

        # Processar palpite
        letras_palpites.append(palpite)
        pilha_palpites.append(palpite)

        if palpite in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    palavra_atual[i] = letra
        else:
            erros += 1

        # Verificar fim de jogo
        if erros == erros_maximos:
            print(f"\nVocê perdeu! A palavra secreta era: {palavra_secreta}")
            break

        if "_" not in palavra_atual:
            print(f"\nParabéns! Você venceu! A palavra era: {palavra_secreta}")
            break

# Iniciar o jogo
jogar()
