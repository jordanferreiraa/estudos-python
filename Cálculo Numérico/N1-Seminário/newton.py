import math as m

#função f(x)
def f(x):
    return x - m.sin(x) - 0.5

#derivada da função f(X)
def fLinha(x):
    return 1 - m.cos(x)

def Newton():
    x0 = 1
    iteracoes = 3
    iteracao = 0
    while iteracao <= iteracoes:
        x1 = x0 - f(x0)/fLinha(x0)
        x0 = x1
        iteracao += 1
    print('\nMétodo de Newton')
    print('A raiz encontrada x = ',x1)
    print('Número de iterações =',iteracao)
    print('f(x) = ',f(x1))

Newton()