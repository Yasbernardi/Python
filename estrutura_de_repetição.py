# -*- coding: utf-8 -*-
"""Estrutura-de-Repetição.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RQZlmwdFvTn5_MUXaKfuVBZHttH63iN_

**1) Faça um algoritmo que:
• leia 20 números inteiros;
• escreva os números que são negativos;
• escreva a média dos números positivos.**
"""

soma = 0
positivos = 0
for i in range(5):
  num = int (input("Digite um número: "))
  if num < 0:
    print (num, "é negativo")
  else:
    soma = soma + num
    positivos = positivos + 1

print ("Média positivos =", soma/positivos)

"""**2) Faça um algoritmo que leia 15 números inteiros e escreva, para cada número lido, se é par ou ímpar.**"""

for i in range(5):
  num = int (input("Digite um número: "))
  if int (num % 2 == 0):
    print ("Seu valor é par")
  else:
    print ("Seu valor é impar")

"""**3) Dado um conjunto de valores inteiros positivos, determinar qual o menor e qual o maior valor do conjunto. Um número com valor “0” (zero) indica o fim dos dados e
não deve ser considerado.**
"""

menor = 9999
maior = -9999
num = 1
while num != 0:
    num = int(input("Digite um número: "))
    if num != 0:
      if num > maior:
        maior = num
      if num < menor:
        menor = num

print("O maior número é", maior)
print("O menor número é", menor)

"""**4) Faça um algoritmo que calcule e escreva a soma dos números pares e a soma dos
números ímpares entre 1 e 100**
"""

somapar = 0
somaimpar = 0
for num in range(1, 101):
  if num % 2 == 0:
    somapar = somapar + num
  else:
    somaimpar = somaimpar + num

print("Soma dos pares é igual a ", somapar)
print("Soma dos impares é igual a ", somaimpar)

"""**5)Faça um algoritmo que leia a altura de 20 pessoas e calcule a média aritmética das alturas.**"""

somaltura = 0
for contador in range (5):
  altura = float(input("Digite a altura: "))
  somaltura = somaltura + altura

mediaaltura = somaltura /5.0
print ("Média das alturas = ", mediaaltura)

"""**6) Faça um algoritmo que leia n valores inteiros e escreva quantos desses valores são negativos.**"""

conta = 0
for i in range(5):
  num = int (input("Digite um número: "))
  if num < 0:
    print (num, "é negativo")
    conta = conta + 1

print ("A quantidade de numeros negativos é ", conta)

"""**7) Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a
caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”. Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui.**
"""

tinta = int (input("Digite a quantidade de tinta da sua caneta: "))
while tinta > 0:
  print("Enquanto tem tinta a caneta escreve...")
  tinta = tinta -2
print ("a tinta da sua caneta acabou :(")

"""**8) Faça um algoritmo que calcule e escreva a soma da seguinte série de 100 termos:**"""

soma = 0 
for num in range (0,100):
  soma = num + soma

print (soma)

"""**9) Construir um algoritmo que calcule o fatorial de um número N.**"""

num= int(input("Digite um número: "))
from math import factorial

print ("O fatorial do número é: ", factorial(num))

"""**10) Calcule os valores de y**"""

x = 1.0
while x <= 5.0:
  y = (3 + (2 * x) + 6 * x ** 2) / (1 + (9 * x) + 16 * x ** 2)
  x = x + 0.1
  print(y)

"""**11)Faça um algoritmo que leia n números inteiros e escreva, para cada número lido, os divisores e quantidade de divisores.**"""

divisores = 1
quantidade_divisores = 1
num = int(input("Informe um valor: "))
while divisores <= num:
    if num % divisores == 0:
        print("{} é dividido por {}. Total de divisores: {}".format(num, divisores, quantidade_divisores))
        quantidade_divisores = quantidade_divisores +1
    divisores = divisores + 1

"""**12) Faça um algoritmo que leia n pares de valores, sendo o primeiro valor o número de inscrição do atleta e o segundo a altura (em cm) do atleta. Escreva:
• o número de inscrição e a altura do atleta mais alto;
• o número de inscrição e a altura do atleta mais baixo;
• a altura média do grupo de atletas.**
"""

alturas = 0
soma_alturas = 0
menor = maior = 0
quantidade = 0
while alturas <= 5:
    inscricao = int(input("Informe a inscrição do atleta: "))
    altura = int(input("Informe a altura do atleta: "))
    alturas = alturas + 1
    soma_alturas = soma_alturas + altura
    media = soma_alturas / alturas
    quantidade = quantidade + 1
    if quantidade ==1:
        maior = menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura

print("A média é {}. Maior altura: {}. Menor altura: {}.".format(media, maior, menor))

"""**13) Os regulamentos de uma competição de pesca impõem um limite no peso total de pesca de um dia. Faça um algoritmo que leia o limite diário (em quilogramas) e então leia o peso (em gramas) de cada peixe e escreva o peso total da pesca obtido até aquele ponto. Quando o limite diário for excedido escreva uma mensagem e encerre a execução do algoritmo. O algoritmo deve ainda apresentar ao usuário a seguinte mensagem: informar o peso de mais um peixe: s (SIM) / n (NÃO)? antes de prosseguir com a entrada de dados.**"""

resposta = "s"
soma_peixes = 0
limite_diario_pesca = int(input("Limite diário (kg): "))
while resposta == "s":
    pesodopeixe = int(input("Peso do peixe (g): "))
    pesodopeixe = pesodopeixe / 1000
    soma_peixes = soma_peixes + pesodopeixe

    if pesodopeixe > limite_diario_pesca:
        print("Peso do peixe superior ao limite diário")
    elif soma_peixes > limite_diario_pesca:
        print("Limite diário atingido")
    else:
        print("A soma atual dos peixes: {}g".format(soma_peixes))

    resposta = str(input("Deseja digitar mais um valor? s (SIM) / n (NÃO) "))

print("Peso dos peixes: {}kg".format(soma_peixes))

"""**14) Faça um algoritmo que leia valores, sendo que cada valor representa a idade de uma
pessoa. Calcule e escreva a idade média do grupo de pessoas. Só devem ser
computados no cálculo valores maiores do que zero. O algoritmo deve apresentar ao usuário a seguinte mensagem: deseja digitar mais um valor: s (SIM) / n (NAO), antes de prosseguir com a entrada de dados.**
"""

resposta = "s"
soma_idades = 0
idades = 0
while resposta == "s":
    idade = int(input("Idade: "))

    if idade == 0:
        print("Valor inválido")
    else:
        soma_idades = soma_idades + idade
        idades = idades + 1
        media = soma_idades / idades
    resposta = str(input("Deseja digitar mais um valor? s (SIM) / n (NÃO) "))

print("A média de idades é: {}".format(media))

"""**15) Uma loja de departamentos oferece para seus clientes um determinado desconto de
acordo com o valor da compra efetuada. O desconto é de 20% caso o valor da compra
seja maior que R$ 500,00 e de 15% caso seja menor ou igual. Faça um algoritmo que
leia, para cada cliente, nome, endereço e valor da compra e escreva o total a pagar.
Um nome de cliente igual a ULTIMO indica o fim da entrada de dados.**
"""

nome_cliente = ""
while nome_cliente != "ULTIMO":
    nome_cliente = str(input("Nome: "))
    endereco_cliente = str(input("Endereço: "))
    valor_compra = int(input("Valor da compra: "))

    if valor_compra > 500:
        desconto = (valor_compra * 20) / 100
        valor_compra = valor_compra - desconto

    if valor_compra <= 500:
        desconto = (valor_compra * 15) / 100
        valor_compra = valor_compra - desconto
    print ("{}. Endereço: {}. Valor da compra com desconto: R${}".format(nome_cliente, endereco_cliente, valor_compra))

print("Fim do Programa")