# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
par = 0
impar = 0
for x in range(10):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Quantidade de números pares: {par}')
print('----------------------------------------')
print(f'Quantidade de números ímpares: {impar}')