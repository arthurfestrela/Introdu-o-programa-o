salario = float(input('Digite o seu salário: '))

if 0 < salario <= 2000:
    print('Isento')
elif 2000 < salario <= 3500:
    imposto = salario * 0.1
    print(imposto)
elif 3500 < salario:
    imposto = salario * 0.15
    print(5imposto)

