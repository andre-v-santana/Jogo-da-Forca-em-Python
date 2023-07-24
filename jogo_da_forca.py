# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 02:02:22 2021

@author: andre
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:45:24 2021

@author: André Santana
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import string
import time
import os

def menu():
    """
    Esta função apresenta o menu e processa a escolha do utilizador
    """
    escolha = int(input("O que deseja fazer?\n\n" +
                        "  1. Registar Jogador\n" +
                        "  2. Registar Palavra\n" +
                        "  3. Exibir Records\n" +
                        "  4. Exibir pontuação de um determinado jogador\n" +
                        "  5. Jogar\n" +
                        "  6. Desafiar o Robô\n" +
                        "  7. Sair\n"))
    
    if escolha == 1:
        
        jogador = ''
        while len(jogador) < 3 or len(jogador) > 10:
            jogador = input("Por favor introduza o nome do jogador que deseja registar (3-10 caracteres, 'back' para voltar ao menu): ")
            if len(jogador) < 3 or len(jogador) > 10:
                print("Nome de jogador inválido!")
                jogador = ''
            elif jogador.upper() == 'BACK':
                menu()
                break
            else:
                with open('jogadores.txt') as ficheiro:
                    if jogador.upper() in ficheiro.read().upper():
                        print(f'O nome "{jogador.upper()}" já se encontra registado!')
                        ficheiro.close()
                        jogador = ''
                    else:
                        with open('jogadores.txt', 'a+') as ficheiro:
                            ficheiro.write('0,' + jogador + "\n")
                            ficheiro.close()
                            confirmacao = ''
                            while confirmacao == '':
                                confirmacao = input("Jogador registado com sucesso! Deseja registar outro jogador? (S/N) ").upper()
                                if confirmacao == 'S':
                                    jogador = ''
                                elif confirmacao == 'N':
                                    menu()
                                else:
                                    confirmacao = print("Entrada inválida!")
                                    confirmacao = ''
                            
    if escolha == 2:
        
        palavra = ''
        while len(palavra) < 3 or len(palavra) > 15 or palavra.upper != 'BACK':
            palavra = input("Por favor introduza uma palavra para registar (3-15 caracteres, 'back' para voltar ao menu): ")
            if len(palavra) < 3 or len(palavra) > 15:
                print("Palavra inválida!")
                palavra = ''
            elif palavra.upper() == 'BACK':
                menu()
                break
            else:
                with open('palavras.txt') as ficheiro:
                    if palavra.upper() in ficheiro.read().upper():
                        print(f'\nA palavra "{palavra.upper()}" já se encontra registada!')
                        ficheiro.close()
                        palavra = ''
                    else:
                        with open('palavras.txt', 'a+') as ficheiro:
                            ficheiro.write(palavra + "\n")
                            ficheiro.close()
                            confirmacao = ''
                            while confirmacao == '':
                                confirmacao = input("Palavra registada com sucesso! Deseja registar outra palavra? (S/N) ").upper()
                                if confirmacao == 'S':
                                    palavra = ''
                                elif confirmacao == 'N':
                                    menu()
                                else:
                                    confirmacao = print("Entrada inválida!")
                                    confirmacao = ''

    if escolha == 3:
        
        with open('jogadores.txt') as ficheiro:
            if os.stat("jogadores.txt").st_size == 0:
                print("\nNão existem pontuações guardadas!\n")
                ficheiro.close()
                menu()
            else:
                conteudo = ficheiro.readlines()
                ficheiro.close()
                dict_pontuacaoJogador = {}
                for linha in conteudo:
                    pontuacao, nome = linha.split(',')
                    dict_pontuacaoJogador[nome.strip()] = int(pontuacao)
                dict_ordenado = sorted(dict_pontuacaoJogador.items(), key=lambda item:item[1], reverse = True)
                print('\nTop 3 pontuações:')
                i = 0
                for nome, pontuacao in dict_ordenado:
                    while i < 3:
                        print(f'\n{nome:^10} : {pontuacao:4} pontos')
                        i += 1
                        break
                time.sleep(2.5)
                menu()

    if escolha == 4:
        
        with open('jogadores.txt') as ficheiro:
            if os.stat("jogadores.txt").st_size == 0:
                print("\nNão existem pontuações guardadas!\n")
                ficheiro.close()
                menu()
            else:
                conteudo = ficheiro.readlines()
                ficheiro.close()
                jogador = ''
                dict_pontuacaoJogador = {}
                for linha in conteudo:
                    pontuacao, nome = linha.split(',')
                    dict_pontuacaoJogador[nome.strip()] = int(pontuacao)
                while jogador.upper() != 'BACK':
                    jogador = input("\nInsira um nome de jogador para ver os seus pontos ('back' para voltar ao menu): ")
                    if jogador not in dict_pontuacaoJogador.keys() and jogador.upper() != 'BACK':
                        print("\nEsse jogador não tem nenhuma pontuação gravada!")
                    else:
                        if jogador.upper() != 'BACK':
                            temp = dict_pontuacaoJogador.get(jogador)
                            print(f'\n{jogador} : {temp} pontos')
                            time.sleep(2.5)
                            menu()
                            break
                
                if jogador.upper() == 'BACK':
                    menu()
                    jogador = ''
                
    if escolha == 5:
        
        with open('jogadores.txt') as ficheiro:
            if os.stat("jogadores.txt").st_size == 0:
                print("\nAntes de jogar, por favor registe o seu nome de jogador!\n")
                ficheiro.close()
                menu()
            else:
                conteudo = ficheiro.readlines()
                ficheiro.close()
                jogador = 'An'
                dict_pontuacaoJogador = {}
                for linha in conteudo:
                    pontuacao, nome = linha.split(',')
                    dict_pontuacaoJogador[nome.strip()] = int(pontuacao)
                while jogador not in dict_pontuacaoJogador.values():
                    jogador = input("\nIntroduza o seu nome do jogador ('back' para voltar ao menu): ")
                    if jogador not in dict_pontuacaoJogador.keys() and jogador != 'back':
                        print("\nEsse jogador não se encontra registado!")
                        
                    elif jogador == 'back':
                        menu()
                        break
                        
                    else:
                        pontos = dict_pontuacaoJogador.get(jogador)
                        palavra = gerar_palavra()
                        jogar(palavra, jogador, pontos)
                        break
                    
    if escolha == 6:
        
        palavra = ''
        while len(palavra) < 3 or len(palavra) > 10 or not palavra.isalpha() or palavra.upper() != 'BACK':
            palavra = input('Introduza a palavra para o robô adivinhar (3-10 caracteres, "back" para voltar ao menu): ')
            if len(palavra) < 3 or len(palavra) > 10 or not palavra.isalpha():
                print('\nPalavra inválida!')
                palavra = ''
            elif palavra.upper() == 'BACK':
                menu()
                break
            else:
                robo(palavra)
                break
                        
    if escolha == 7:
        
        confirmacao = ''
        while confirmacao == '':
            confirmacao = input("Deseja mesmo sair do jogo? (S/N) ").upper()
            if confirmacao == "S":
                print("\nObrigado por jogar!")
                break
            elif confirmacao == "N":
                menu()
                break
            else:
                print("Entrada inválida!")
                confirmacao = ''
          
########################################################################################
def gerar_palavra():
    '''
    Esta função gera uma palavra aleatória, contida no ficheiro 'palavras'
    e retorna-a em letras maiusculas (para ser fácilmente comparada posteriormente).
    '''
    if os.stat("palavras.txt").st_size == 0:
        print("\nNão existem palavras guardadas. Por favor registe algumas palavras antes de começar um jogo!\n")
        menu()
    else:
        linha = open('palavras.txt').read().splitlines()
        palavra = random.choice(linha)
        return palavra.upper()
    
########################################################################################
def jogar(palavra, jogador, pontos):
    """
    Esta é a função que simula o jogo da forca
    """
    palavra_por_descobrir = ("_" * len(palavra))
    adivinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6
    
    print(f'\n{jogador} : {pontos} pontos')
    print("\nBoa sorte!\n")
    print(imprimir_boneco(tentativas))
    print("Palavra: \n")
    for letra in palavra_por_descobrir:
        print(letra + " ", end='')
    print("\n\nLetras escolhidas: \n")
    print(*sorted(letras_utilizadas))
    
    while not adivinhou and tentativas > 0:
        tentativa = input("Por favor introduza uma letra ou uma palavra: ").upper()
        if len(tentativa) == 1 and tentativa.isalpha():
            if tentativa in letras_utilizadas:
                print(f'Já tentou a letra "{tentativa}", por favor tente outra!')
            elif tentativa not in palavra:
                print(f'\nA letra "{tentativa}" não pertence à palavra!')
                tentativas -= 1
                letras_utilizadas.append(tentativa)
            else:
                print(f'\nBem jogado! "{tentativa}" pertence à palavra!')
                letras_utilizadas.append(tentativa)
                palavra_como_lista = list(palavra_por_descobrir)
                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for index in indices:
                    palavra_como_lista[index] = tentativa
                palavra_por_descobrir = "".join(palavra_como_lista)
                if "_" not in palavra_por_descobrir:
                    adivinhou = True
                
        elif len(tentativa) == len(palavra) and tentativa.isalpha():
            if tentativa in palavras_utilizadas:
                print(f"Já tentou a palavra '{tentativa}', por favor tente outra!")
            elif tentativa != palavra:
                print(f'"{tentativa}" não é a palavra correcta!')
                tentativas -= 1
                palavras_utilizadas.append(tentativa)
            else:
                adivinhou = True
                palavra_por_descobrir = palavra
        else:
            print("Tentativa inválida, tente outra vez!")
            
        print(imprimir_boneco(tentativas))
        print("Palavra: \n")
        for letra in palavra_por_descobrir:
            print(letra + " ", end='')
        print("\n\nLetras que já experimentou: \n")
        print(*sorted(letras_utilizadas))
        
    if adivinhou:
        pontosGanhos = tentativas * 10
        pontos += pontosGanhos    
        
        actualizar_resultado(jogador, pontos)
        print(f'\nParabéns! "{palavra}" é a palavra certa! Ganhou {pontosGanhos} pontos! Tem agora {pontos} pontos!')
        
        jogar_outra_vez(palavra, jogador, pontos)
    else:
        pontos -= 10
        print("\nVocê perdeu :(")
        print(f'\nA palavra correcta era "{palavra}"! Perdeu 10 pontos, tem agora {pontos} pontos!')
        
        jogar_outra_vez(palavra, jogador, pontos)
        
########################################################################################
        
def actualizar_resultado(jogador, novaPontuacao):
    """
    Esta função encarrega-se de actualizar o resultado do jogador no ficheiro
    """
    
    linhas = []
    nomes = []
    pontuacoes = []

    with open('jogadores.txt', 'r') as ficheiro:
        conteudo = ficheiro.readlines()
        ficheiro.close()
        for linha in conteudo:
            linhas.append(linha.strip())
            pontuacao, nome = linha.split(',')
            nomes.append(nome.strip())
            pontuacoes.append(pontuacao)

    indices = [x for x in range(len(nomes)) if jogador in nomes[x]]
    for indice in indices:
        indice = int(indice)

    nome_temp = nomes[indice]
    del nomes[indice]
    del pontuacoes[indice]

    with open('jogadores.txt', 'w') as ficheiro:
        for i in range(len(nomes)):
            ficheiro.write(f'{pontuacoes[i]}' + ',')
            ficheiro.write(f'{nomes[i]}' + '\n')
        ficheiro.write(f'{novaPontuacao}' + ',')
        ficheiro.write(f'{nome_temp}' + '\n')
    ficheiro.close()
        
########################################################################################
    
def jogar_outra_vez(palavra, jogador, pontos):
    """
    Esta função encarrega-se de começar uma nova partida, caso o utilizador assim o deseje
    """
    
    confirmacao = input("Jogar outra vez? (S/N) ")
    while confirmacao.upper() != "S":
        if confirmacao.upper() == 'N':
            menu()
            break
        else:
            print('\nEntrada inválida!')
            confirmacao = ''    
    if confirmacao.upper() == 'S':       
        palavra = gerar_palavra()
        jogar(palavra, jogador, pontos)
    
########################################################################################
        
def robo(palavra):
    """
    Esta função tenta adivinhar uma palavra introduzida pelo jogador
    """
    palavra_por_descobrir = ("_" * len(palavra))
    letras_utilizadas = []
    tentativas = 6
    adivinhou = False
    
    print(imprimir_boneco(tentativas))
    print('\nPalavra: \n')
    for letra in palavra_por_descobrir:
        print(letra + " ", end='')
    print("\n\nLetras escolhidas pelo robô: \n") 
    print(*sorted(letras_utilizadas))
    
    
    while not adivinhou and tentativas > 0:
        
        tentativa = random.choice(string.ascii_letters)
        
        if tentativa.upper() in palavra.upper():
            
            letras_utilizadas.append(tentativa.upper())
            palavra_como_lista = list(palavra_por_descobrir)
            indices = [i for i, letra in enumerate(palavra) if letra.upper() == tentativa.upper()]
            for index in indices:
                palavra_como_lista[index] = tentativa.upper()
            palavra_por_descobrir = "".join(palavra_como_lista)
            if "_" not in palavra_por_descobrir:
                adivinhou = True
            time.sleep(1)
        
        elif tentativa.upper() in letras_utilizadas:
            tentativa = random.choice(string.ascii_letters)
            
        else:
            letras_utilizadas.append(tentativa.upper())
            time.sleep(1)
            tentativas -= 1
        
        time.sleep(1)
        print(imprimir_boneco(tentativas))
        print('\nPalavra: \n')
        for letra in palavra_por_descobrir:
            print(letra + " ", end='')
        print("\n\nLetras escolhidas pelo robô: \n") 
        print(*sorted(letras_utilizadas))
        
    if adivinhou:
        if tentativas == 1:
            print(f"\nO robô venceu com {tentativas} tentativa restante! :)")
            time.sleep(2.5)
            menu()
        else:
            print(f"\nO robô venceu com {tentativas} tentativas restantes! :)")
            time.sleep(2.5)
            menu()
    else:
        print("\nO robô não conseguiu adivinhar a palavra! :(")
        time.sleep(2.5)
        menu()
        
########################################################################################
def imprimir_boneco(tentativas):
    """
    Esta função imprime o 'tabuleiro' do jogo correspondente a cada tentativa
    """
    
    fases = ["""
   ---------.
   ||       |
   ||       O
   ||      \|/
   ||       |
   ||      / \ 
   ||
----------------------
                 
   """,
   """
   ---------.
   ||       |
   ||       O
   ||      \|/
   ||       |
   ||      /  
   ||
----------------------

   """,
   """
   ---------.
   ||       |
   ||       O
   ||      \|/
   ||       |
   ||  
   ||
----------------------

   """,
   """
   ---------.
   ||       |
   ||       O
   ||      \|
   ||       |
   || 
   ||
----------------------
    
   """,
   """
   ---------.
   ||       |
   ||       O
   ||       |
   ||       |
   || 
   ||
----------------------

   """,
   """
   ---------.
   ||       |
   ||       O
   ||
   ||
   ||
   ||
----------------------
                 
   """,
   """
   ---------.
   ||       |
   ||
   ||
   ||
   ||
   ||
----------------------

   """
    ]
    return fases[tentativas]               

########################################################################################
def main():
    print("\nBem-vindo ao meu jogo da forca!")
    menu()

#para correr no cmd        
if __name__ == "__main__":
    main()