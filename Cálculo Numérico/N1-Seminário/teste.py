import math as m
#import sympy 
#from sympy.plotting import*

#x = sympy.Symbol('x')
#funcao = x - m.sin(x) - 0.5
#plot(funcao,(x,-2,2))


#def f(x):
#    f = 5 * m.sin(x) - x**4
#    return f

def bissecao(f,a,b,tal,iteMax):
    cont = 0
    FA = f(a)
    FB = f(b)
    while cont <= iteMax:
        x = (a+b)/2
        print(x)
        FX = f(x)

        if abs(f(x)) < tal:
            print(f'\nMétodo da Bisseção \nA raiz aproximada = {x}\nO número de iterações = {cont}\nf(x) = {f(x)} ')
            return x, cont

        if FA * FX > 0:
            a = x
            FA = FX
        else:
            b = x
            FB = FX
        cont += 1
    return 'O método falhou depois de '+str(cont) + 'iterações'

#bissecao(f,1,2,10**-4,100)

def f(x):
    return 5 * m.sin(x) - x**4

def fLinha(x):
    return 5 * m.cos(x) - 4 * (x**3)

def Newton():
    x0 = 1
    iteracoes = 5
    iteracao = 0
    while iteracao <= iteracoes:
        x1 = x0 - f(x0)/fLinha(x0)
        x0 = x1
        iteracao += 1
    print('Método de Newton')
    print('A raiz encontrada x = ',x1)
    print('Número de iterações = ',iteracao)
    print('f(x) = ',f(x1))

Newton()