class NumeradorZeroError(Exception):
    pass

try:
    x = int(input("Digite um número: "))
    divisão = x / 10
    if x == 0:    
        raise NumeradorZeroError("O número digitado é 0, favor informar outro número.")
    
except NumeradorZeroError as e:
    print(e)
    
else:
    print("O resultado da divisão é" , divisão)