Lado1 = int(input('Digite o tamanho do primeiro lado: '))
Lado2 = int(input('Digite o tamanho do segundo lado: '))
Lado3 = int(input('Digite o tamanho do terceiro lado: '))

if Lado1 == Lado2 == Lado3:
    print('Seu triangulo é equilátero')

elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
    print('Seu triangulo é Isóceles')

elif Lado1 != Lado2 != Lado3:
    print('Seu triangulo é escaleno')