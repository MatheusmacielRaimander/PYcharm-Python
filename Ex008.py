metro = float(input('Quantos metros para fazer a conversão: '))
print('A conversão de medidas para metros foi: {}, milimetros mm {:.0f}, centimetros cm {:.0f}, decimetros dm {:.0f},'.format(metro,(metro*1000),(metro*100),(metro*10)))
print('Decamêtro dam {}, Hectômetro hm {}, Quilômetro km {}.'.format((metro/10),(metro/100),(metro/1000)))