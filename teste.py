músicas = []
pontos_totais = 0
tentativas_totais = 0

print("Bem vindo ao jogo da forca do ye!")
total_músicas = int(input())

for i in range(total_músicas):
  if i == 1:
      pass
  música = input()
  músicas += [música]
  música = músicas[i]
  if i != total_músicas - 1:
      print(f"Esta é a música {i + 1} de {total_músicas}.")
  else:
      print("Última música!")
  resposta = ''
  for caractere in música:
      if caractere != ' ':
          resposta += '_'
      else:
          resposta += ' '
  tentativas = 0
  for caractere in música:
      if caractere != ' ':
          tentativas += 2
  tentativas_feitas = 0
  letras_corretas = ''
  while tentativas_feitas < tentativas and '_' in resposta:
      chute = input()
      tentativas_feitas += 1
      letra_chute = chute[0]
      chute = letra_chute
      chute_correto = False
      for caractere in música:
          if caractere == chute:
              chute_correto = True
      if chute_correto:
          if chute not in letras_corretas:
              print("Uhuuuuu! Consegui adivinhar uma letra!")
              letras_corretas += chute
              n_resposta = ''
              for j in range(len(música)):
                  if música[j] == chute:
                      n_resposta += chute
                  else:
                      n_resposta += resposta[j]
              print("Resposta atual:", n_resposta)
              resposta = n_resposta
          else:
              print("Já tinha colocado essa letra antes, preciso de mais atenção.")
              print("Resposta atual:", n_resposta)
      else:
        n_resposta = resposta
        for j in range(len(música)):
            if música[j] == chute:
                n_resposta += chute
        print(f"Eita! Parece que a letra {chute} não está na música secreta!")
        print("Resposta atual:", n_resposta)
  if '_' not in resposta:
      pontos_totais += 1
      print("Isso! Consegui acertar uma música!")
  else:
    print(f"Vish, essa tava difícil, a música era {música}. Espero acertar a próxima!")
  tentativas_totais += tentativas

print(f"Consegui acertar {pontos_totais} músicas de {total_músicas}!")

taxa_sucesso = pontos_totais / total_músicas

if taxa_sucesso <= 0.5:
    print("Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!")
elif taxa_sucesso <= 0.75:
    print("Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.")
elif taxa_sucesso < 1.0:
    print("Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.")
else:
    print("Eu sou o próprio Kanye West.")