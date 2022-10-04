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

# método dos trapezios simples para integração númerica
def metodoTrapeziosSimples(a, b, funcao, dif2_funcao):
    # definindo valor de h
    h = b - a

    # calculando pelo método dos trapézios simples
    integralTrapeziosSimples = (h*(funcao(b) + funcao(a)))/2.00
    # imprimindo o resultado da integração
    print("\nO valor da integral pelo método dos trapezios simples é = %.6f " %
          (integralTrapeziosSimples))

    # computando o valor do erro
    # lisnpace pega em dois intervalos e divide em uma quantidade de partes
    vetorIteracaoErro = np.linspace(a, b, b) 
    # aplicando a derivada segunda no vetor iteração erro
    def funcaoVetorIteracaoErro(x): return dif2_funcao(x)
    # armazenando o resultado em um vetor
    vetorResultadoErro = np.vectorize(funcaoVetorIteracaoErro)
    vetorResultadoErro = vetorResultadoErro(vetorIteracaoErro)

    # calculando o erro
    # (h^3/12) * maximo valor absoluto do vetorResultadoErro
    erro = (pow(h,3)/12.00) * max(abs(vetorResultadoErro))
    #imprimindo o erro
    print("O valor do erro pelo método dos trapezios simples é menor ou igual que = %.6f" %erro)

metodoTrapeziosSimples(0,2,funcao,dif2_funcao)

#método dos trapézios repetido para integração numérica
def metodoTrapeziosRepetidos(a,b,n,funcao,dif2_funcao):
    #definindo valor de h
    h = (b-a)/n

    #gerando o vetor igualmente espaçado para efetuar as iterações
    # lisnpace pega em dois intervalos e divide em uma quantidade de partes
    vetorIteracao = np.linspace(a,b,n+1)

    #excluindo os extremos de integração para o vetor gerado
    index = [0,n]
    vetorIteracao = np.delete(vetorIteracao,index)
    vetorIteracao = vetorIteracao

    #aplicando a função do vetor de integração
    funcaoVetorIteracao = lambda x: funcao(x)
    #vetorizando os resultados e armazenando no vetorResultado
    vetorResultado = np.vectorize(funcaoVetorIteracao)

    #armazenandio vetor resultado
    vetorResultado = vetorResultado(vetorIteracao)

    #calculando pelo método dos trápezios repetidos
    integralTrapeziosRepetido = (funcao(a) + funcao(b) + 2*sum(vetorResultado)) * (h/2.00)
    #imprimindo o resultado da integração
    print("\n")
    print(f'O valor da integral pelo método dos trapezios repetido é = {integralTrapeziosRepetido}')

    #computando o valor do erro
    vetorIteracaoErro = np.linspace(a,b,n+1)

    #aplicando a derivada segunda do vetor iteração erro
    funcaoVetorIteracaoErro = lambda x: dif2_funcao(x)

    #armazenando o resultado em um vetor
    vetorResultadoErro = np.vectorize(funcaoVetorIteracaoErro)
    vetorResultadoErro = vetorResultadoErro(vetorIteracaoErro)

    #calculando o erro
    # ((b-a^3) * maximo valor absoluto do vetorResultadoErro) / (12 * n^2)
    erro = (pow(b-a,3)*max(abs(vetorResultadoErro))) / (12.00*n*n)
    #imprimindo o erro
    print("O valor do erro pelo método dos trapezios repetido é menor ou igual que = %.6f" %erro)
    print("\n")

metodoTrapeziosRepetidos(0,2,4,funcao,dif2_funcao)
