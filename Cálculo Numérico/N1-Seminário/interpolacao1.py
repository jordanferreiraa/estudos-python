#biblioteca para trabalhar de modo simbolico
import sympy
z = sympy.Symbol('z')
sympy.init_printing()
#biblioteca numerica
import numpy as np 
#biblioteca gráfica
import matplotlib.pyplot as plt 

#x=[-2, -1, 0]  y=[19.1, 3.99, -1]
#Interpolação Quadrática: P(x) = Ax**2 + Bx + C

#A(-2)**2 + B(-2) + C = 19.1
#A(-1)**2 + B(-1) + C = 3.99
#A(0)**2 + B(0) + C = -1

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

#pontos
x = [-2, -1, 0]
y = [19.1, 3.99, -1]
#grau da interpolação
n = 2
#ponto qualquer, valor inicial
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


tam = len(x)
yp = interpoLagrange(xp,x,y,n)
#variavel para fazer o gráfico
t = np.arange(x[0],x[tam-1]+0.5,0.1)
#lista para armazenar cada valor de t
yt = []
#pegar cada valor de t e chamar a função interpolação
for i in t:
    yt.append(interpoLagrange(i,x,y,n))

#curva contínua azul
plt.plot(t,yt,'b-')
#pontos vermelhos
plt.plot(x,y,'ro')
#ponto verde para qual estou realizando uma estimativa
plt.plot(xp,yp,'g*')
#exibir malha
plt.grid()
#exibindo gráfico
plt.show()
    