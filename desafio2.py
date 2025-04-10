numero = int(input("Digite um número para calcular a tabuada: "))


with open("tabuada.txt", "w") as arquivo:

    for i in range(1, 11):
        resultado = numero * i
        arquivo.write(f"{numero} x {i} = {resultado}\n")

print("A tabuada foi salva no arquivo 'tabuada.txt'.")