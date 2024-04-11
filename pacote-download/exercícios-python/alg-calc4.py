custo_et = float(input('Digite o custo do espetáculo'))
custo_in = float(input('Digite o valor do ingresso'))
qtd_in = custo_et//custo_in
qtd_lucro = (custo_et*0.23 + custo_et)//custo_in
print(f'A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado é {qtd_in}')
print(f'A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23% é {qtd_lucro}')
