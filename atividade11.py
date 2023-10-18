# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Digite a distância da sua viagem em Km/h: "))
preco1 = distancia * 0.5
preco2 = distancia * 0.45
if distancia <= 200:
    print("O preço da sua viagem é: R$", preco1)
else:
    print("O preço da sua viagem é: R$", preco2)