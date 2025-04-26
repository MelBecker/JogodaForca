from cores import Colors, Style

def boneco_forca(palavra_aleatoria):
    palavra = palavra_aleatoria
    quantidade_letras = len(palavra)
    nova_palavra = palavra.replace(" ", "-")
    erro = 0
    perdeu = 6

    if erro == 0:
        print(Style.BOLD + Colors.BLUE + "________________")
        print(Colors.GREEN + "|")
        print("|")
        print("|")
        print("|")
        print("| ", Colors.BLACK + quantidade_letras * "_ ")
    elif erro == 1:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|")
        print("|")
        print("|")
        print("| ", Colors.BLACK + quantidade_letras * "_ ")
    elif erro == 2:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|              |")
        print("|")
        print("|")
        print("| ", Colors.BLACK + quantidade_letras * "_ ")
    elif erro == 3:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|")
        print("|")
        print("|")
        print("| ", Colors.BLACK + quantidade_letras * "_ ")
    elif erro == 4:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|\\")
        print("|")
        print("|")
        print("| ", Colors.BLACK + quantidade_letras * "_ ")
    elif erro == 5:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|\\")
        print("|             /")
        print("|") 
        print("| ", Colors.BLACK + quantidade_letras * "_ ")
    elif erro == perdeu:
        print(Colors.BLUE + "________________")
        print(Colors.GREEN + "|              O")
        print("|             /|\\")
        print("|             / \\")
        print("|")
        print("| ", Colors.BLACK + quantidade_letras * "_ ")