clubes = []
for i in range (5):
    nome = input(f'Digite o nome do {i+1}º clube: ')
    clubes.append(nome)

clube_procurado = input('\nDigite o nome do clube que deseja procurar: ')
clubes_minusculo = [clube.lower() for clube in clubes]
clube_procurado_minusculo = clube_procurado.lower()
if clube_procurado in clubes: 
    print('ACHEI')
else:
    print('NÃO ACHEI')    