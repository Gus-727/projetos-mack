def atualiza_preco(valor):
    valor_somado = valor + (valor * 0.10)
    return valor_somado

def taxa(valor):
    valor_taxa = valor + (valor * 2.5/100)
    valor_taxa2 = valor_taxa - valor
    return valor_taxa2

def entrada():
    return float(input('Digite o valor'))

def main():
    valor = entrada()
    valor = atualiza_preco(valor)
    print('O valor do produto com acréscimo é ', round(valor, 2))
    res = taxa(valor)
    print('O acréscimo tem valor de ', round(res, 2))
main()

# def atualiza_preco(valor):
#     valor = valor * 1.1
#     return valor
# def taxa(valor):
#     tax = valor*0.025
#     return tax

# def main ():
#     valor = float(input())
#     valor = atualiza_preco(valor)
#     tax = taxa(valor)
#     print ("%.2f" %valor)
#     print ("%.2f" %tax)

# main()