laps = int(input())
clima = str(input())
dif = str(input())
pneu = str(input())

if((clima == 'sol') and (pneu == 'chuva')):
  x = (50 - (laps * 15))

elif((clima == 'chuva') and (pneu == 'macio')):
  x = (50 - (laps * 15))
  
elif((clima == 'chuva') and (pneu == 'medio')):
  x = (70 - (laps * 15))
  
elif((clima == 'chuva') and (pneu == 'duro')):
  x = (90 - (laps * 15))
  
else:
  if((clima == 'sol') and ((dif == 'baixa') or (dif == 'media')) and (pneu == 'macio')):
    x = (50 - (laps * 2))
  elif((clima == 'sol') and ((dif == 'baixa') or (dif == 'media')) and (pneu == 'medio')):
    x = (70 - (laps * 2))
  elif((clima == 'sol') and (dif == 'alta') and (pneu == 'macio')):
    x = (50 - (laps * 3))
    
  elif((clima == 'sol') and (dif == 'alta') and (pneu == 'medio')):
    x = (70 - (laps * 3))
  
  elif((clima == 'sol') and (dif == 'alta') and (pneu == 'duro')):
    x = (90 - laps)
  
  elif((clima == 'chuva') and (dif == 'baixa') and (pneu == 'chuva')):
    x = (50 - laps)
    
  elif((clima == 'chuva') and (dif == 'media') and (pneu == 'chuva')):
    x = (50 - (laps * 2))
    
  elif((clima == 'chuva') and (dif == 'alta') and (pneu == 'chuva')):
    x = (50 - (laps * 3))
    
  else:
    x = (19)
  

if(x >= 20):
  print('A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {}.' .format(x))
else:
  print('Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.'.format(x))

  
