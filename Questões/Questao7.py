#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, 
# I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

KWH = int(input("Digite o valor de kWh : "))

print()
print("-------Menu-------")
print("Digite R para residências")
print("Digite I para indústrias")
print("Digite C para comércio")
print("------------------")
print("Qual o tipo de intalação?")
opcao = input("Escolha uma das opções : ")

if opcao == "R":
    if KWH > 500:
        valorPagar = KWH*0.65
        print("O valor a pagar é %.2f"%valorPagar)
    else:
        valorPagar = KWH*0.40
        print("O valor a pagar é %.2f"%valorPagar)
        
elif opcao == "C":
    if KWH > 1000:
        valorPagar = KWH*0.60
        print("O valor a pagar é %.2f"%valorPagar)
    else:
        valorPagar = KWH*0.55
        print("O valor a pagar é %.2f"%valorPagar)
                
elif opcao == "I":
    if KWH > 5000:
        valorPagar = KWH*0.60
        print("O valor a pagar é %.2f"%valorPagar)
    else:
        valorPagar = KWH*0.55
        print("O valor a pagar é %.2f"%valorPagar)
else:
    print("Opção invalida!!")