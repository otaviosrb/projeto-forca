import os
from random import choice

palavras = ["COMPUTADOR", "PROGRAMADOR", "DESAFIO", "TECNOLOGIA", "ALGORITMO",
 "INTELIGENCIA", "PYTHON", "APRENDIZADO", "INTERNET", "DESENVOLVIMENTO"]
PALAVRA = choice(palavras)
tentativas = 6
palavra_codificada = '*' * len(PALAVRA)
letras_erradas = []
letras_certas = []

print(' JOGO DA FORCA '.center(50, '='))
while tentativas > 0:
    print()
    print(f'Tentativas: {tentativas}')
    print(f'Letras erradas: {", ".join(letras_erradas)}')
    letra = input ('Digite uma letra: ').upper()
    os.system('cls')
    if letra == '' or letra == ' ':
        print('Digite algo!')
        print(palavra_codificada)
        continue
    validacao_alfa = letra.isalpha()
    if len(letra) > 1:
        print('Digite apenas UMA letra')
        print(palavra_codificada)
        continue
    if validacao_alfa == False:
        print('Digite apenas LETRAS')
        print(palavra_codificada)
        continue
    if letra in letras_certas:
        print('Esta letra já foi verificada, tente outra!')
        print(palavra_codificada)
        continue
    if letra in PALAVRA:
        letras_certas.append(letra)
        for i in range(len(PALAVRA)):
            if PALAVRA[i] == letra:
                palavra_codificada = palavra_codificada[:i] + letra + palavra_codificada[i+1:]
        print(palavra_codificada)
    if letra not in PALAVRA:
        if letra not in letras_erradas:
            letras_erradas.append(letra)
        else:
            print('Você já tentou essa letra!')
            print(palavra_codificada)
            continue
        tentativas -= 1
        print(palavra_codificada)
    if palavra_codificada == PALAVRA:
        os.system('cls')
        print('VOCÊ GANHOU, PARABÉNS!!')
        print(f'A palavra era: {PALAVRA}')
        exit()
os.system('cls')
print('Você perdeu, não foi dessa vez!')