num1 = int(input("Informe um número:"))
num2 = int(input("Informe um número:"))
num3 = int(input("Informe um número:"))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("O maior eh:",maior,"\n e o menor:",menor)