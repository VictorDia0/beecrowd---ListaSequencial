valor = int(input())
ano = valor // 365
valor = valor - ano * 365
meses = valor // 30
valor = valor - meses * 30
dias = valor
print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')