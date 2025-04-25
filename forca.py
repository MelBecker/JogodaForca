
def boneco_forca(palavra_aleatoria):
    palavra = palavra_aleatoria
    quantidade_letras = len(palavra)
    erros = 0
    perdeu = 6

    letra = input("\nEscolha uma letra: ")
    letra = letra.lower()

    if erros == 0:
        print("__________")
        print("|")
        print("|")
        print("|")
        print("|")
        print("| ", quantidade_letras * "_ ")
    elif erros == 1:
        print("__________")
        print("|         O")
        print("|")
        print("|")
        print("|")
        print("| ", quantidade_letras * "_ ")
    elif erros == 2:
        print("__________")
        print("|         O")
        print("|         |")
        print("|")
        print("|")
        print("| ", quantidade_letras * "_ ")
    elif erros == 3:
        print("__________")
        print("|         O")
        print("|        /|")
        print("|")
        print("|")
        print("| ", quantidade_letras * "_ ")
    elif erros == 4:
        print("__________")
        print("|         O")
        print("|        /|\\")
        print("|")
        print("|")
        print("| _ _ _ _ _ _")
    elif erros == 5:
        print("__________")
        print("|         O")
        print("|        /|\\")
        print("|        /")
        print("|")
        print("| ", quantidade_letras * "_ ")
    elif erros == perdeu:
        print("__________")
        print("|         O")
        print("|        /|\\")
        print("|        / \\")
        print("|")
        print("| ", quantidade_letras * "_ ")