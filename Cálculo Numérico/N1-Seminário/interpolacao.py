import numpy as np
import matplotlib.pyplot as plt

def interpLagrange(xp,x,y,grau):
  yp = 0
  for k in range(0,n+1):
    p = 1
    for j in range(0,n+1):
      if k != j:
        p = p*(xp - x[j])/(x[k] - x[j])

    yp = yp + p * y[k]

  return yp

x = [-2, -1, 0]
y = [19.1, 3.99, -1]

n  = 2
xp = -0.5
yp = interpLagrange(xp,x,y,n)
#t  = np.arange(-1.0,2.0,0.1)
t  = np.arange(-2.0,0.0,0.1)
yt = []
for i in t:
  yt.append(interpLagrange(i,x,y,n))

plt.plot(t,yt,'b-')
plt.plot(x,y,'ro')
plt.plot(xp,yp,'g*')
plt.show()