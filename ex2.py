frase = input("Informe uma frase: ")

try:
    assert frase.isupper()
    print("Frase contem apenas letras Maíusculas")

except AssertionError:
    print("A frase contém letras minúsculas.")
    