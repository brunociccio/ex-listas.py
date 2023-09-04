import os
'''
# EXERCÍCIOS:
Nesta atividade você deve desenvolver dois subalgoritmo e um “programa principal” que permita ao usuário
a manipulação das problemáticas das Funções.
Utilize SOMENTE o conteúdo (métodos) aprendidos em aula (Não utilize recursos não explicados).
## FUNÇÃO 1:
Faça um subalgoritmo chamado converte_vogais_maiusculo(frase) que passe uma frase por
parâmetro e retorne a mesma frase com SOMENTE as vogais maiúsculas.
Veja um exemplo desta função sendo aplicada:
frase = “Testando o funcionamento do subalgoritmo.”
print(converte_vogais_maiusculo(frase))
>> TEstAndO O fUncIOnAmEntO dO sUbAlgOrItmo.
## FUNÇÃO 2:
Faça uma função chamada isfloat(valor) que passe um valor do tipo string por parâmetro e
retorne True caso este valor represente um número float ou False caso não represente.
Veja um exemplo desta função sendo aplicada:
resp = isfloat(“Edson”)
>> False
resp = isfloat(“45.78”)
>> True
resp = isfloat(“78”)
>> True
resp = isfloat(“234.”)
>> True
resp = isfloat(“234,67”)
>> False
resp = isfloat(“12.567.34”)
>> False
## TELAS DO PROGRAMA:
Para desenvolver o programa principal e as rotinas que aplicam as funções, respeite a aparência das
telas sugeridas abaixo:

### Tela 1: Menu:
0 – SAIR
1 – Converte vogais
2 – Verifica se é float
Opção: _
O menu deve conter a chamada para cada função e a opção de encerrar (SAIR) do programa:
1 – Converte vogais:
Uma vez assinalada a Opção: 1, o programa pedirá ao usuário a digitação de uma frase em uma
variável string. Após a digitação, será aplicada a função converte_vogais_maiusculo(frase) e,
logo depois, apresentará a frase conforme os requisitos do enunciado da FUNÇÃO 1.

### Tela 2: 1 – Converte vogais
Digite um texto: Estou fazendo a atividade 1
EstOU fAzEndO A AtIvIdAdE 1
Logo depois de executar a Opção 1, volta ao Menu.
2 – Verifica se é float:
Uma vez assinalada a Opção: 2, o programa pedirá ao usuário a digitação de um valor em uma variável
string. Após a digitação, será aplicada a função isfloat(valor). Caso o valor corresponda a um
número float, exibir a mensagem: “Este valor é float.”, senão exibir a mensagem “Este valor não é
float.”. Teste os exemplos contidos na definição da FUNÇÃO 1.

### Tela 3: 2 – Verifica se é float (cenário 1).
Digite um valor: 234.5
Este valor é float.

### Tela 4: 2 – Verifica se é float (cenário 2).
Digite um valor: 34.6y5
Este valor não é float.
Após a execução da Opção 2, volta ao Menu.
A opção 0 – Sair, termina a execução do programa.
'''

def converte_vogais_maiusculo(frase: str) -> str:
    for letra in frase:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            frase = frase.replace(letra, letra.upper())
    return frase

def isfloat(valor: str) -> bool:
    teste_valor = valor.replace('.','',1)
    if teste_valor.isnumeric():
        return True
    else:
        return False
    
def rodar_sistema():
    while True:
        print(f"""
            MENU
            0 - SAIR
            1 - Converte vogais
            2 - Verifica se é Float
            """)
        opcao = input("Opção: ")
        
        if opcao == '0':
            print("Encerrando o programa.")
            break
        elif opcao == '1':
            print("\n1 - Converte vogais")
            texto = input("Digite um texto: ")
            resultado = converte_vogais_maiusculo(texto)
            print(resultado)
        elif opcao == '2':
            print("\n2 - Verifica se é float")
            valor = input("Digite um valor: ")
            if isfloat(valor):
                print("Este valor é float.")
            else:
                print("Este valor não é float.")
        else:
            print("Opção inválida. Escolha uma opção válida.")

rodar_sistema()