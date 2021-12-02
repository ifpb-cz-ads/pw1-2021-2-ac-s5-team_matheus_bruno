#5) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada.

num1 = int(input("Digite um numero interio : "))
num2 = int(input("Digite outro numero interio : "))
print()
print("-------Menu-------")
print("Digite 1 para somar os dois numeros")
print("Digite 2 para subtrair os dois numeros")
print("Digite 3 para multiplicar os dois numeros")
print("Digite 4 para dividir os dois numeros")
print("------------------")

operacao = int(input("Escolha uma das opções : "))

if operacao == 1:
    soma = num1 + num2
    print("A soma dos numero é %d"%soma)
elif operacao == 2:
    subtrair = num1 - num2
    print("A subtrair dos numero é %d"%subtrair)
elif operacao == 3:
    multiplicação = num1 * num2
    print("A multiplicação dos numero é %d"%multiplicação)
elif operacao == 4:
    divisao = float(num1 / num2)
    print("A divisao dos numero é %.2f"%divisao)
else:
    print("Opção invalida!")