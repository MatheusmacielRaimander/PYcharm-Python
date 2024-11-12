real = float(input('Quanto dinheiro você tem na carteira: '))
dolar = real / 5.67
print('Com R$ {} você pode comprar U${:.2f}'.format(real, dolar))