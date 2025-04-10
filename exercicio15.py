numero = int(input('Digite um número: '))

for m in range (1, 11):
    resultado = numero * m
    print(f'{numero} x {m} = {resultado}')

print('---Solução com while---')
ciclos = 1
while ciclos <= 10:
    resultado = numero * ciclos
    print(f'{numero} x {ciclos} = {resultado}')
    # Increamento
    ciclos +=1