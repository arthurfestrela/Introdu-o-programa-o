import random
Q = [random.randint(1, 10000) for i in range(1, 20)]
print(Q)

maior_valor = max(Q)
posicao_maior = Q.index(maior_valor)

menor_valor = min(Q)
posicao_menor = Q.index(menor_valor)

print(f'O maior valor é {maior_valor} e está na posição {posicao_maior}')
print(f'O menor valor é {menor_valor} e está na posição {posicao_menor}')