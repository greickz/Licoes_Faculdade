# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
for x in range(num1 + 1, num2, 1 ):
    print(x)