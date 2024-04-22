n = int(input('Digite um número natural'))
while n <= 0:
    print('VALOR INVÁLIDO')
    n = int(input('Digite um número natural'))
print(f'Os divisores de {n} são:')
for i in range(1, n+1):
    if n % i == 0:
        print('{}'.format(i), end=' ')
    
