import math as m

def f(x):
    f = x - m.sin(x) - 0.5
    return f

def falsaPosicao(f,a,b,erro,iteMax):
    cont = 0
    FA = f(a)
    FB = f(b)
    while cont <= iteMax:
        x = (a * FB - b * FA) / (FB - FA)
        print(x)
        FX = f(x)

        if abs(f(x)) < erro:
            print(f'\nMetodo da falsa posição \nA raiz aproximada = {x} \nO número de iterações = {cont} \nf(x) = {f(x)} ')
            return x, cont
        if FA * FX > 0:
            a = x
            FA = FX
        else:
            b = x
            FB = FX
        cont += 1
    return 'O metodo falhou depois de '+str(cont) + 'iterações'

falsaPosicao(f,1,2,200**-1,100)