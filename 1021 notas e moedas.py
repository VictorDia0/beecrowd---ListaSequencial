notas = float(input())

cem = notas // 100
notas = notas - cem * 100

cinquenta = notas // 50
notas = notas - cinquenta * 50

vinte = notas // 20
notas = notas - vinte * 20

dez = notas // 10
notas = notas - dez * 10

cinco = notas // 5
notas = notas - cinco * 5

dois = notas  // 2
notas = notas - dois * 2

um = notas // 1
notas = notas - um
um=float('%.2f'% um)
notas=float('%.2f'% notas)

moeda50 = notas // 0.5
notas = notas - moeda50 * 0.5
moeda50=float('%.2f'% moeda50)
notas=float('%.2f'% notas)

moeda25 = notas // 0.25
notas = notas - moeda25 * 0.25
moeda25=float('%.2f'% moeda25)
notas=float('%.2f'% notas)

moeda10 = notas // 0.10
notas = notas - moeda10 * 0.10
moeda10=float('%.2f'% moeda10)
notas=float('%.2f'% notas)

moeda5 = notas // 0.05
notas = notas - moeda5 * 0.05
moeda5=float('%.2f'% moeda5)
notas=float('%.2f'% notas)

moeda1 = notas * 100
moeda1=float('%.2f'% moeda1)
notas=float('%.2f'% notas)
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(cem)))
print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(vinte)))
print('{} nota(s) de R$ 10.00'.format(int(dez)))
print('{} nota(s) de R$ 5.00'.format(int(cinco)))
print('{} nota(s) de R$ 2.00'.format(int(dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(um)))
print('{} moeda(s) de R$ 0.50'.format(int(moeda50)))
print('{} moeda(s) de R$ 0.25'.format(int(moeda25)))
print('{} moeda(s) de R$ 0.10'.format(int(moeda10)))
print('{} moeda(s) de R$ 0.05'.format(int(moeda5)))
print('{} moeda(s) de R$ 0.01'.format(int(moeda1)))
