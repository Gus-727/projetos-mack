n = int(input('Digite um número para que seja exibido a sua tabuada'))
while n < 0:
    print('VALOR INVÁLIDO')
    n = int(input('Digite um número para que seja exibido a sua tabuada'))
for c in range(1, 11, 1):
    res = c * n
    print('{} x {} = {}'.format(n, c, res))
