#biblioteca para trabalhar de modo simbolico
import sympy
z = sympy.Symbol('z')
sympy.init_printing()

#biblioteca numerica
import numpy as np 

#biblioteca gráfica
import matplotlib.pyplot as plt 

#função para imprimir polinômio de lagrange
def polinomioLagrange(xp,x,y,grau):
    yp = 0
    for k in range(0,n+1):
        p = 1
        for j in range(0,n+1):
            if k != j:
                p = p*(z - x[j]) / (x[k] - x[j])
        
        yp = yp + p * y[k]

    return yp

#dados de entrada
x = [-2, -1, 0]
y = [19.1, 3.99, -1]
#grau da interpolação
n = 2
xp = -0.5
p = polinomioLagrange(xp,x,y,n)
p

#fazer o gráfico da interpolação
def interpoLagrange(xp,x,y,grau):
    #valor inicial do ponto
    yp = 0
    for k in range(0,n+1):
        p = 1
        for j in range(0,n+1):
            if k != j:
                p = p*(xp - x[j]) / (x[k] - x[j])

        yp = yp + p * y[k]

    return yp

x = [-2, -1, 0]
y = [19.1, 3.99, -1]

tam = len(x)
#grau da interpolação
n = 2
#ponto qualquer
xp = -0.5
yp = interpoLagrange(xp,x,y,n)
t = np.arange(x[0],x[tam-1]+0.5,0.1)
yt = []
for i in t:
    yt.append(interpoLagrange(i,x,y,n))

plt.plot(t,yt,'b-')
plt.plot(x,y,'ro')
plt.plot(xp,yp,'g*')
plt.show()
    