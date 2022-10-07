nome = input()
salarioFixo = float(input())
valorVendas = float(input())

comissao = valorVendas * 0.15
total = salarioFixo + comissao

print(f'TOTAL = R$ {total:.2f}')