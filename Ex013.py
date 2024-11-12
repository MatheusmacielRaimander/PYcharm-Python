sal = float(input('Qual é o salário do Funcionario? R$ '))
novo = sal + (sal*15/100)
print('O novo salario R${}, com aumento 15% passar a receber R${:.2f}'.format(sal,novo))