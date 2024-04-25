
clima = str(input())

if(clima == 'chuvoso'):
    pista_molhada = input()
    if pista_molhada == 'True':
        pista_molhada = True
    else:
        pista_molhada = False

temp = str(input())
desp = str(input())
pos = int(input())

print('Estratégia de prova de Max Verstappen!')

if((clima == 'ensolarado') and (temp == 'alta')):
  print('Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!')
elif((clima == 'ensolarado') and (temp != 'alta')):
  print('Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.')
elif((clima == 'nublado') and (temp == 'alta')):
  print('Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!')
elif((clima == 'nublado') and ((temp == 'baixa') or (temp == 'moderada'))):
  print('Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!')
elif((clima == 'chuvoso') and (pista_molhada == True)):
  print('Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.')
elif((clima == 'chuvoso') and (pista_molhada == False)):
  print('Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!')
  
if(pos == 1) and (desp == 'bom'):
  print('Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.')
elif(pos == 1) and (desp == 'ruim'):
  print('Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.')
elif(1 < pos <= 12):
  print('Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
elif(pos > 12):
  print('Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
