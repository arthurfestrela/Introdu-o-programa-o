import time

bd_filmes = []

def cadastra_filmes(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd
def lista_filmes(bd):
    for i in range (len(bd)):
        print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

def altera_filmes(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd


while True:
    print('1 - Cadastrar Filme')
    print('2 - Listar Filmes')
    print('2 - Alterar Filme')
    op = int(input('Digite sua opção: '))

    if op == 1:
        titulo = input('Digite o titulo do filme: ')
        ano = int(input('Digite o ano do filme: '))

        bd_filmes = cadastra_filmes(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano
        )

        print('Filme cadastrado!')
    elif op == 2:

        print('Filmes listados!')
    elif op == 3:
        lista_filmes()
        i = int(input('Qual filme deseeja alterar?: '))
        titulo = input('Digite o novo titulo: ')
        ano = int(input('Digite o novo ano: '))
        
        print('Filme alterado!')
    else:
        print(f'Opção {op} inválida!')

    time.sleep(3)




