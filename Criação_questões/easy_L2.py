#Boas práticas de programação
pratica_1, pts_pratica_1 = 'Programar utilizando uma boa IDE', 3
pratica_2, pts_pratica_2 = 'Códigos limpos e organizados', 10
pratica_3, pts_pratica_3 = 'Nomenclatura objetiva e de fácil identificação de variáveis', 7
pratica_4, pts_pratica_4 = 'Assistir às aulas do REDU', 10
pratica_5, pts_pratica_5 = 'Comentários significativos', 5
pratica_6, pts_pratica_6 = 'Evitar repetições desnecessárias de códigos', 5
pratica_7, pts_pratica_7 = 'Tirar dúvidas com os monitores e professores', 10

#Más práticas de programação
pratica_8, pts_pratica_8 = 'Programar sem utilizar IDE', -5
pratica_9, pts_pratica_9 = 'Código bagunçado e mal estruturado', -6
pratica_10, pts_pratica_10 = 'Nomenclatura confusa e difícil de identificar variáveis', -5
pratica_11, pts_pratica_11 = 'Não tirar dúvidas com professores e monitores ', -10

qtd_combinacoes = int(input())
pontuacao_total = 0

if not qtd_combinacoes == 0:

    for _ in range(qtd_combinacoes):
        pratica = input()

        if pratica == pratica_1:
            pontuacao_total += pts_pratica_1

        elif pratica == pratica_2:
            pontuacao_total += pts_pratica_2

        elif pratica == pratica_3:
            pontuacao_total += pts_pratica_3

        elif pratica == pratica_4:
            pontuacao_total += pts_pratica_4

        elif pratica == pratica_5:
            pontuacao_total += pts_pratica_5

        elif pratica == pratica_6:
            pontuacao_total += pts_pratica_6

        elif pratica == pratica_7:
            pontuacao_total += pts_pratica_7

        elif pratica == pratica_8:
            pontuacao_total += pts_pratica_8

        elif pratica == pratica_9:
            pontuacao_total += pts_pratica_9

        elif pratica == pratica_10:
            pontuacao_total += pts_pratica_10

        elif pratica == pratica_11:
            pontuacao_total += pts_pratica_11

    if pontuacao_total < 0:
        pontuacao_total = 0

    media_geral = pontuacao_total / qtd_combinacoes
    if media_geral > 10:
        media_geral = 10

else:
    media_geral = 0

if media_geral < 3:
    print('É melhor voltar a cantar mesmo!')

elif media_geral > 3 and media_geral < 7:
    print('Vai precisar se esforçar um pouco mais, meu cantor!')

elif media_geral == 7:
    print('Na conta certa!')

elif media_geral > 7 and media_geral < 9:
    print('Nasceu para programar!')

else:
    print('Já pode ser chamado de Kanye, the dev, West!')