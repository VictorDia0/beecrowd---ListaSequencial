notas = int(input())
print(notas)
cem = notas//100
notas = notas - cem * 100

cinq = notas//50
notas = notas - cinq * 50

vinte = notas//20
notas = notas - vinte * 20

dez = notas//10
notas = notas - dez * 10

cinco = notas//5
notas = notas - cinco * 5

dois = notas//2
notas = notas - dois * 2

um = notas//1
notas = notas - um * 1
print(f'{cem} nota (s) de R$ 100,00')
print(f'{cinq} nota (s) de R$ 50,00')
print(f'{vinte} nota (s) de R$ 20,00')
print(f'{dez} nota (s) de R$ 10,00')
print(f'{cinco} nota (s) de R$ 5,00')
print(f'{dois} nota (s) de R$ 2,00')
print(f'{um} nota (s) de R$ 1,00')
