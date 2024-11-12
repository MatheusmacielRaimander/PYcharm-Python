km = float(input('A velocidade do carro atingiu? '))
if km > 80:
    print('Multado. Por excesso de velocidade, o limite permitido é 80km/h')
    multaa = (km-80)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multaa))
print('Tenha um bom dia! Dirija com segurança!')