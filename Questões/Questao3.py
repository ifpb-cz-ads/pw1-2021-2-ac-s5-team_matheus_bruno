# 3) Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, de 15%.

salario = float(input("Digite seu salario atual: "))

if salario > 1250.00:
    aumento = salario + (salario *0.10)
    print("Seu salario atual é %.2f"%aumento)
else:
    aumento = salario + (salario *0.15)
    print("Seu salario atual é %.2f"%aumento)