class Tamanho_STR_Excecao(Exception):
    pass

try:
    str1 = (input("Digite a Primeira String: "))
    str2 = (input("Digite a Segunda String "))

    if len(str1) != len(str2):
        raise Tamanho_STR_Excecao("O Comprimento das Duas Strings são diferentes, favor informar condicentes")
    
except Tamanho_STR_Excecao as e:
    print(e)
    
else:
    print("Tamanho das Duas Strings são Iguais")