#1 - função para receber o nome completo
def receber_nome_completo():
    return input("Digite um nome completo: ")

#2 - função para separar o nome do sobrenome
def separar_nome_sobrenome(nome_completo: str) -> str:
    partes_nome = nome_completo.split(' ')
    nome = partes_nome[0]
    sobrenome = ' '.join(partes_nome[1:])
    return nome, sobrenome

#3 - função para contar quantas palavras tem o nome completo
def conta_palavras(nome_completo: str) -> str:
    numero_palavras = 1
    for caractere in nome_completo:
        if caractere == ' ': #analisar
            numero_palavras += 1
    return numero_palavras

#4 - função composta para exibir o nome de forma bibliografica
#4.1
def ultimo_sobrenome(texto: str) -> str:
    posicao_ultimo_sobrenome = -1
    for i, caractere in enumerate(texto):
        if caractere == ' ': #analisar
            posicao_ultimo_sobrenome = i
    return posicao_ultimo_sobrenome
#4.2
def formato_bibliografico(nome_completo: str) -> str:
    sobrenome_pos = ultimo_sobrenome(nome_completo)
    sobrenome = nome_completo[sobrenome_pos +1:].upper()
    nome = nome_completo[:sobrenome_pos]
    return f"{sobrenome}, {nome}"

#função para rodar o menu
def rodar_sistema():
    while True:
        print(f"""
            MENU
            0 - SAIR
            1 - Digite um nome completo
            2 - Exibe o Nome separado do Sobrenome
            3 - Conta quantas palavras há no nome completo
            4 - Exibir em formato de bibliografia
            """)
        opcao = input("Digite a opção desejada: ")
        if opcao == '0':
            print("Encerrando o sistema!")
            break
        elif opcao == '1':
            nome_completo = receber_nome_completo()
        elif opcao == '2':
            if nome_completo == "":
                print("Primeiramente digite um nome na opção 1!")
            else:
                nome, sobrenome = separar_nome_sobrenome(nome_completo)
                print(f"Nome: {nome}")
                print(f"Sobrenome: {sobrenome}")
        elif opcao == '3':
            if nome_completo == "":
                print("Primeiramente digite um nome na opção 1!")
            else:
                numero_palavras = conta_palavras(nome_completo)
                print(f"O nome {nome_completo} tem {numero_palavras} palavras")
        elif opcao == '4':
            if nome_completo == "":
                print("Primeiramente digite um nome na opção 1!")
            else:
                bibliografia = formato_bibliografico(nome_completo)
                print(bibliografia)
        else:
            print("Opção inválida, digite um item de 0 a 4.")
rodar_sistema()
