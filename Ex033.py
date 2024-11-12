a= int(input('Primeiro Valor: '))
b= int(input('Segundo Valor: '))
c= int(input('Terceiro valor: '))
#Verificar quem é menor
menor= a
if b<a and b<c:
    menor =b
if c<a and c<b:
    menor = c

#Verificar quem é o maior
maior= a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior= c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))