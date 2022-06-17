from datetime import datetime

hora = datetime.now()
hora_formateada = hora.strftime('%I,%M %p')

print (f'Son las: {hora_formateada}')

if hora.hour>=19:
  print ('Es momento de ir a casa')

else:
  print  ('Podrás irte a casa en:',(18- hora.hour), 'horas y', (59-hora.minute),'minutos')
