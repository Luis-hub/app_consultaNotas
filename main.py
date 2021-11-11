a = int(input('Primeiro Bimestre'))
b = int(input('Segunda Bimentre'))
c = int(input('Terceiro Bimentro'))
d = int(input('Quarto Bimentre'))

media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10: 
  print('meida: {}' .format(media))
else:
  print('voce nao alcancaou a media')