import random
from cores import Style, Colors
from temas import TEMAS

def mensagem_bemvindo():
    print(Style.BOLD + Colors.RED + "Bem-vindo ao Jogo da Forca!" + Style.RESET)

def iniciacao_jogo():
    while True:
        iniciar = input(Style.HEADER + "Deseja jogar(s/n)? ")
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

if __name__ == "__main__":
    mensagem_bemvindo()
    jogar = iniciacao_jogo()
    if not jogar:
        exit()
    tema = selecione_temas()
    random_number = random.randint(0, len(TEMAS[tema]) - 1)
    print(TEMAS[tema][random_number])