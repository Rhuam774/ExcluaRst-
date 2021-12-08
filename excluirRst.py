arquivo = input('\n\nQual o nome do arquivo: ')
while True:
    texto = open(arquivo, 'r')
    print('\n=================================================================================\n')
    excluir1 = input('Digite um caractere chave para excluir apartir dele nas linhas:')
    print('\n=================================================================================\n\nEscolha uma opcao:')
    excluir2 = input('\n(1) excluir deste caractere para frente\n(2) excluir deste caractere para tras\ndigite uma opcao:')
    print('\n=================================================================================\n')
    texto1 = open(f'{arquivo.split(".")[0]}_editado.txt', 'w')
    L = 0
    if excluir2 == '1':
        L = 0
    elif excluir2 == '2':
        L = 1

    for lin in texto:
        print(lin.split(excluir1)[L])
        texto1.write(lin.split(excluir1)[L]+'\n')
    texto.close()
    texto1.close()

