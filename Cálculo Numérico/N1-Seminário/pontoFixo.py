import math as m

#função f(x)
def f(x):
    return x - m.sin(x) - 0.5

#função iteração g(x)
def g(x):
    return m.sin(x) + 0.5

def pontoFixo():
    x0 = 1      
    iteracoes = 15
    iteracao = 0
    while iteracao <= iteracoes:
        x1 = g(x0)
        x0 = x1
        iteracao += 1
    print('\nMétodo do Ponto Fixo ')
    print('A raiz encontrada foi x = ',x1)
    print('Número de iterações = ', iteracao)
    print('f(x) = ',f(x1))
    print('g(x) = ',x1)

pontoFixo()