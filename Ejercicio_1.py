frase_usuario = input("Dime una frase: ")


vocales = ["a", "e", "i", "o", "u"]
espacios = [" "]
signos = ["@", ",", "."]



n_vocales = 0
n_espacios = 0
n_consonantes = 0
n_signos = 0


for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1

    elif letra in espacios:
        n_espacios += 1

    elif letra in signos:
        n_signos += 1

    else:
        n_consonantes += 1


print("las vocales: {}".format(n_vocales))
print("las espacios: {}".format(n_espacios))
print("las consonantes: {}".format(n_consonantes))
print("las signos: {}".format(n_signos))

