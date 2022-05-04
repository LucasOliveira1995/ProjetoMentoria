nome = str(input('Digite o nome do funcionário: '))
for c in range(0, 6):
    print('''Aqui você escolhe sobre qual assunto deseja tratar a avaliação:
    [ 1 ] Performance 
    [ 2 ] Valores Da Empresa
    [ 3 ] Treinamento
    [ 4 ] Escelência Técnica e Funcional
    [ 5 ] Trabalho em Equipe
    [ 6 ] Entrega e Resultados''')
    print('Nota: 0 á 10')
    escolha = int(input('O que deseja avaliar: '))
    if escolha == 1:
        print('O funcionários executa seu trabalho atendendo aos padrões da empresa?')
        n1 = int(input('Nota: '))
        print('Contribui com sugestões de melhoria dos processos e serviços da empresa?')
        n2 = int(input('Nota: '))
    if escolha == 2:
        print('Demostra os valores da empresa no dia a dia de trabalho?')
        n3 = int(input('Nota: '))
        print('Participa das iniciativas que a empresa oferece?')
        n4 = int(input('Nota: '))
    if escolha == 3:
        print('Demostra os conhecimentos necessários para atuar na área?')
        n5 = int(input('Nota: '))
        print('Participa efetivamente das ações de treinamento e conscientização de sua área?')
        n6 = int(input('Nota: '))
    if escolha == 4:
        print('Demostra conhecimento, analisa criticamente o processo e busca aperfeiçoamento técnico?')
        n7 = int(input('Nota: '))
    if escolha == 5:
        print('Respita, ouve, ajuda e valoriza os colegas de trabalho?')
        n8 = int(input('Nota: '))
        print('Comunica-se de maneira clara, concisa e trasnparente?')
        n9 = int(input('Nota: '))
    if escolha == 6:
        print('Cumpre os objetivos estabelecidos para si e suporta os colegas para o atingimentos dos objetivos?')
        n10 = int(input('Nota: '))
        print('Dentre de seu escopo de trabalho, toma decisões adequadas seguindo os procedimentos, dados e fatos?')
        n11 = int(input('Nota: '))
print('Fim do programa')