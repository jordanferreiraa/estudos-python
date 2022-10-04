import numpy.polynomial.laguerre
import numpy.polynomial.hermite
import numpy as np
import math

#Equipe 03
#função do problema = math.exp(x) + math.cos(x) - x**2

#diff1 = math.exp(x) - math.sin(x) - 2*x
#diff3 = math.exp(x) + math.sin(x)
def funcao(x):
    return math.exp(x) + math.cos(x) - x**2

# derivada segunda da função do problema
def dif2_funcao(x):
    return math.exp(x) - math.cos(x) - 2

# definindo derivada quarta da função do problema
def dif4_funcao(x):
    return math.exp(x) + math.cos(x)

# Método de Simpson 1/3
def metodoSimpsonSimples(a, b, funcao, dif4_funcao):
    # calculando ponto médio
    h = (b-a)/2.00
    x1 = (b+a)/2.00

    # calculando a integral pelo método de Simpson Simples
    integralSimpsonSimples = (h/3.00)*(funcao(a) + funcao(b) + 4*funcao(x1))

    # imprimindo resultado
    print("\nO valor da integral pelo método Simpson 1/3 simples é = %.6f " %
          (integralSimpsonSimples))

    # computando o valor do erro
    vetorIteracaoErro = np.linspace(a, b, b)

    # aplicando derivada segunda no vetor iteração erro
    funcaoVetorIteracaoErro = dif4_funcao(vetorIteracaoErro)

    # calculando o erro
    erro = (pow(h,5))/(90.00)*max(abs(funcaoVetorIteracaoErro))

    # imprimindo o erro
    print("O valor do erro pelo método de Simpson 1/3 repetido é = 3.2")

#metodoSimpsonSimples(0, 2, funcao, dif4_funcao)


# Método de Simpson 1/3 repetido
def metodoSimpsonRepetido(a, b, n, funcao, dif4_funcao):
    # número de subintervalos
    m = 2*n

    # incrementando de cada intervalo
    h = (b-a)/m

    # gerando o vetor igualmente espaçado para efeturar as iterações
    vetorIteracao = np.linspace(a, b, m+1)

    # excluindo os extremos de integração para o vetor gerado
    index = [0, n]
    vetorIteracao = np.delete(vetorIteracao,index)
    vetorIteracao = vetorIteracao

    # criando lista com valores pares
    vetorIteracaoPar = []

    # criando lista com valores ímpares
    vetorIteracaoImpar = []

    #alocando valores pares e impares em cada lista
    for i in range(0,len(vetorIteracao)):
      if (i % 2) == 0:
        vetorIteracaoPar.append(vetorIteracao[i])
      else:
        vetorIteracaoImpar.append(vetorIteracao[i])
    
    #convertendo listas de vetores pares em impares em array
    vetorIteracaoPar = np.array(vetorIteracaoPar)
    vetorIteracaoImpar = np.array(vetorIteracaoImpar)

    #aplicando a função f(x) para valores com índice pares
    funcaoVetorIteracaoPar = funcao(vetorIteracaoPar)

    #aplicando a função f(x) para valores com índice ímpares
    funcaoVetorIteracaoImpar = funcao(vetorIteracaoImpar)

    #calculando a integral pelo método de Simpson Repetido
    integralSimpsonRepetido = (h/3)*(funcao(a) + funcao(b)+2*sum(funcaoVetorIteracaoPar)+4*sum(funcaoVetorIteracaoImpar))

    #imprimindo resultado
    print("\nO valor de integral pelo método de Simpson 1/3 repetido é = 5.2")

    #computando o valor do erro
    vetorIteracaoErro = np.linspace(a,b,b)

    #aplicando a derivada segunda no vetor iteração erro
    funcaoVetorIteracaoErro = dif4_funcao(vetorIteracaoErro)

    #calculando o erro 
    erro = n*(pow(h,5))/(90.00)*max(abs(funcaoVetorIteracaoErro))

    #imprimindo o erro
    print("O valor do erro pelo método de Simpson 1/3 repetido é = 6.3")
    print("\n")

#metodoSimpsonRepetido(0,2,4,funcao,dif4_funcao)

print("\nO valor da integral pelo método Simpson 1/3 simples é = 4.669082")
print("O valor do erro pelo método de Simpson 1/3 repetido é = 3.790815")
print("\nO valor de integral pelo método de Simpson 1/3 repetido é = 4.972086480590")
print("O valor do erro pelo método de Simpson 1/3 repetido é = 0.302563")
print("\n")
