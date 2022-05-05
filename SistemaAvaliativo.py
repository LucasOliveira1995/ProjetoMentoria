nome = str(input('Digite o nome do funcionário: '))
print('*' * 70)
print('''Aqui você escolhe sobre qual assunto deseja tratar a avaliação:
[ 1 ] Performance 
[ 2 ] Valores Da Empresa
[ 3 ] Treinamento
[ 4 ] Escelência Técnica e Funcional
[ 5 ] Trabalho em Equipe
[ 6 ] Entrega e Resultados''')
while True:
    print('''[ 0 ] Mostar opções novamente
[999] Finalizar Avaliação''')
    escolha = int(input('O que deseja avaliar: '))
    if escolha == 1:
        print('-- PERFORMANCE --')
        print('O funcionários executa seu trabalho atendendo aos padrões da empresa?')
        n1 = float(input('Nota: '))
        print('Contribui com sugestões de melhoria dos processos e serviços da empresa?')
        n2 = float(input('Nota: '))
    if escolha == 2:
        print('-- VALORES DA EMPRESA --')
        print('Demostra os valores da empresa no dia a dia de trabalho?')
        n3 = float(input('Nota: '))
        print('Participa das iniciativas que a empresa oferece?')
        n4 = float(input('Nota: '))
    if escolha == 3:
        print('-- TREINAMENTOS --')
        print('Demostra os conhecimentos necessários para atuar na área?')
        n5 = float(input('Nota: '))
        print('Participa efetivamente das ações de treinamento e conscientização de sua área?')
        n6 = float(input('Nota: '))
    if escolha == 4:
        print('-- EXCELÊNCIA TÉCNICA E FUNCIONAL --')
        print('Demostra conhecimento, analisa criticamente o processo e busca aperfeiçoamento técnico?')
        n7 = float(input('Nota: '))
    if escolha == 5:
        print('-- TRABALHO EM EQUIPE --')
        print('Respita, ouve, ajuda e valoriza os colegas de trabalho?')
        n8 = float(input('Nota: '))
        print('Comunica-se de maneira clara, concisa e trasnparente?')
        n9 = float(input('Nota: '))
    if escolha == 6:
        print('-- ENTREGA E RESULTADOS --')
        print('Cumpre os objetivos estabelecidos para si e suporta os colegas para o atingimentos dos objetivos?')
        n10 = float(input('Nota: '))
        print('Dentre de seu escopo de trabalho, toma decisões adequadas seguindo os procedimentos, dados e fatos?')
        n11 = float(input('Nota: '))
    if escolha == 0:
        print('''[ 1 ] Performance 
[ 2 ] Valores Da Empresa
[ 3 ] Treinamento
[ 4 ] Escelência Técnica e Funcional
[ 5 ] Trabalho em Equipe
[ 6 ] Entrega e Resultados''')
    if escolha == 999:
        break
media = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11)/11
print('*' * 70)
print('Analisando o funcionário {}, vimos que sua média é {:.1f}!'.format(nome, media))
if media <= 5:
    print(f'O funcionário {nome} precisa passar por alguns treinamentos para melhor desempenho e seu crescimento dentro da empresa!')
if 5 < media <= 7:
    print(f'O funcionário {nome} está dentro dos parâmetros da empresa, é de extrema decisão de seu superior se quer treina-lo para melhor ou não!')
if media > 7:
    print(f'Parabens o funcionário {nome} está em ótimo desenvolvimento na empresa, merecendo ser olhado com carinho para futuras promoções!')