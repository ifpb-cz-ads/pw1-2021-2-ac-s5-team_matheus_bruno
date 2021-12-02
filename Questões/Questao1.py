#1) Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = int(input("Digite a velocidade do seu carro: "))

if velocidade > 80:
    calculo = (velocidade - 80) * 5
    print("Voce sera multado, o valor da multa é %d reais" %calculo)
else: 
    print("Sua velocidade é %d"%velocidade)