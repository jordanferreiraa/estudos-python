import math as m

def f(x):
    return x - m.sin(x) - 0.5

def metodoBissecao():
    a = float(input('Digite o limite inferior a: '))
    b = float(input('Digite o limite superior b: '))
    iteracoes = int(input('Digite o número de iterações: '))
    iteracao = 0
    if f(a)*f(b) < 0:
        while iteracao <= iteracoes:
            c = (a+b)/2
            if f(a)*f(b) < 0:
                b = c
            elif f(b)*f(c) < 0:
                a = c
            iteracao += 1
        print('A raiz encontrada foi x = ',c)
        print('f(x) = ',f(c))
    else:
        print('Não há raizes neste intervalo: ')

metodoBissecao()
