nome = str(input('Digite o nome do funcionário: '))
for c in range(0, 4):
    print('''Aqui você escolhe sobre qual assunto deseja tratar a avaliação:
    [ 1 ] Objetivos 
    [ 2 ] Performance
    [ 3 ] Competências
    [ 4 ] Evolução''')
    print('Nota: 0 á 10')
    escolha = int(input('O que deseja avaliar: '))
    if escolha == 1:
        print('Os objetivos do funcionário está de acordo com os objetivos que a empresa propoe à ele?')
        nota1 = float(input('Nota: '))
        print('O funcionário concorda com a proposta que a empresa fornece à ele?')
    #if escolha == 2:

    #if escolha == 3:

    #if escolha == 4:
