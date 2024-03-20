class MinhaExcecao(Exception):
    pass

try:
    x = int(input("Informe o nº: "))
    if x % 2 != 0:
        raise MinhaExcecao("O número digitado é IMPAR, favor informar um número par.")
    
except MinhaExcecao as e:
    print(e)
    
else:
    print("O número digitado é par")