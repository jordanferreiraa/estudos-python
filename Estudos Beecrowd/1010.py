cod, num, valor = input().split()
cod = int(cod)
num = int(num)
valor = float(valor)

cod2, num2, valor2 = input().split()
cod2 = int(cod2)
num2 = int(num2)
valor2 = float(valor2)

total = (num*valor)+(num2*valor2)

print(f'VALOR A PAGAR: R$ {total:.2f}')