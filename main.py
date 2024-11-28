import os
from random import choice

palavras = ["computador", "programador", "desafio", "tecnologia", "algoritmo",
            "inteligencia", "python", "aprendizado", "internet", "desenvolvimento"]
PALAVRA = choice(palavras)
tentativas = 0
palavra_codificada = '*' * len(PALAVRA)

print(' JOGO DA FORCA '.center(50, '='))
print()
while palavra_codificada != PALAVRA:
    letra = input ('Digite uma letra: ').lower()
    validacao_alfa = letra.isalpha()
    tentativas += 1
    if len(letra) > 1:
        print('Digite apenas UMA letra')
    if validacao_alfa == False:
        print('Digite apenas LETRAS')
    if letra in PALAVRA:
        for i in range(len(PALAVRA)):
            if PALAVRA[i] == letra:
                palavra_codificada = palavra_codificada[:i] + letra + palavra_codificada[i+1:]
        print(palavra_codificada)
os.system('cls')
print('VOCÊ GANHOU, PARABÉNS!!')
print(f'A palavra era: {PALAVRA}')
print(f'Tentativas: {tentativas}')