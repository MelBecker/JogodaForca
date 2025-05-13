import random
import re
from cores import Style, Colors
from temas import TEMAS
from consts import HEADER, MAX_ERROS

g_erro = 0
g_palpite = ""

def mensagem_bemvindo():
    print(Colors.MAGENTA + HEADER)    
    print(Style.BOLD + Colors.RED + "Bem-vindo ao Jogo da Forca!" + Style.RESET)

def iniciacao_jogo():
    while True:
        iniciar = input(Style.HEADER + Colors.WHITE + "Deseja jogar(s/n)? ")
        iniciar = iniciar.lower()
        if iniciar == "s":
            return True
        elif iniciar == "n":
            return False

def selecione_temas():
    print(Style.BOLD + Colors.MAGENTA + "\nTemas" + Style.RESET)
    for indice, valor in enumerate(TEMAS, start = 1): 
        print(f"{indice}. {valor}")
    
    while True:
        indice_tema = input(f"Escolha um tema (1-{len(TEMAS)}): ")
        if indice_tema.isnumeric():
            indice_tema = int(indice_tema)
            if indice_tema in range(1, len(TEMAS) + 1):
                temas = list(TEMAS.keys())
                tema = temas[indice_tema - 1]
                return tema

def selecione_palavra_aleatoria(tema): 
    random_number = random.randint(0, len(TEMAS[tema]) - 1)
    return TEMAS[tema][random_number]

def selecione_letra():
    letra = input(Style.RESET + Colors.WHITE + "\nEscolha uma letra: ")
    letra = letra.lower()
    
    while True:
        if letra in palavra_aleatoria:
            indices = [match.start() for match in re.finditer(letra, palavra_aleatoria)]
            print(indices)
            return indices
        elif letra not in palavra_aleatoria:
            return
        

def boneco_forca(tamanho_palavra_aleatoria):

    if g_erro == 0:
        print(Style.BOLD + Colors.BLUE + "________________")
        print(Colors.GREEN + "|")
        print("|")
        print("|")
        print("|")
        print("| ", Colors.BLACK + tamanho_palavra_aleatoria * "_ ")
    elif g_erro == 1:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|")
        print("|")
        print("|")
        print("| ", Colors.BLACK + tamanho_palavra_aleatoria * "_ ")
    elif g_erro == 2:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|              |")
        print("|")
        print("|")
        print("| ", Colors.BLACK + tamanho_palavra_aleatoria * "_ ")
    elif g_erro == 3:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|")
        print("|")
        print("|")
        print("| ", Colors.BLACK + tamanho_palavra_aleatoria * "_ ")
    elif g_erro == 4:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|\\")
        print("|")
        print("|")
        print("| ", Colors.BLACK + tamanho_palavra_aleatoria * "_ ")
    elif g_erro == 5:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|\\")
        print("|             /")
        print("|") 
        print("| ", Colors.BLACK + tamanho_palavra_aleatoria * "_ ")
    elif g_erro == MAX_ERROS:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|\\")
        print("|             / \\")
        print("|")
        print("| ", Colors.BLACK + tamanho_palavra_aleatoria * "_ ")



if __name__ == "__main__":
    mensagem_bemvindo()
    jogar = iniciacao_jogo()
    if not jogar:
        exit()
    tema = selecione_temas()
    random_number = random.randint(0, len(TEMAS[tema]) - 1)
    palavra_aleatoria = selecione_palavra_aleatoria(tema)
    print(palavra_aleatoria)
    g_palpite = len(palavra_aleatoria) * "_ "
    espacos_palavra = palavra_aleatoria.replace(" ", "-")
    while (True):
        boneco_forca(len(palavra_aleatoria))
        selecione_letra()