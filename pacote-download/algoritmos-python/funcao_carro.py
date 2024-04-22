def entrada_carro(carro):
    for i in range (0, 4):
        modelo = input('Digite o modelo do carro')
        carro.append(modelo)
    return carro

def entrada_consumo(consumo):
    for i in range (0, 4):
        cons = int(input('Digite quantos litros o carro gasta por km'))
        consumo.append(cons)
    return consumo

def economico(cons, modelo):
    if cons[0] > cons[1] and :
        carro_econ = modelo[0]
    elif cons[1] > cons[0,2,3]:
        carro_econ = modelo[1]
    elif cons[2] > cons[0,1,3]:
        carro_econ = modelo[2]
    elif cons[3] > cons[0,1,2]:
        carro_econ = modelo[3]
    return carro_econ
    

def main():
    carro = []
    consumo = []
    modelo = entrada_carro(carro)
    cons = entrada_consumo(consumo)
    econ = economico(cons, modelo)
    print('O carro mais economico é ', econ)
main()