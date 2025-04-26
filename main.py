import random
from cores import Style, Colors
from temas import TEMAS
from consts import HEADER
from forca import boneco_forca

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
            posicao = palavra_aleatoria.find(letra)
        elif letra not in palavra_aleatoria:
            return 

if __name__ == "__main__":
    mensagem_bemvindo()
    jogar = iniciacao_jogo()
    if not jogar:
        exit()
    tema = selecione_temas()
    random_number = random.randint(0, len(TEMAS[tema]) - 1)
    palavra_aleatoria = selecione_palavra_aleatoria(tema)
    print(palavra_aleatoria)
    boneco_forca(palavra_aleatoria)
    selecione_letra()