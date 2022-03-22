casa = {}
orientaciones = ['NORTE', 'SUR', 'ESTE', 'OESTE']

class Casa():
  global casa
  def Paredes(self, orientacion):
    for i in range(len(orientacion)):
      nombre = orientacion[i]
      casa[nombre] = {
          'ventanas': {},
      }
    print(casa)
    Casa().Ventanas([['NORTE', 0.5, ''], ['SUR', 1, ''], ['ESTE', 2, ''], ['OESTE', 1, '']])
  def Ventanas(self, ventanas):
    dimensiones = []
    for i in range(len(ventanas)):
      nombre = ventanas[i][0]
      casa[nombre]['ventanas'] = {
        'superficie': ventanas[i][1],
        'proteccion': ventanas[i][2]
      }
      dimensiones.append(ventanas[i][1])  
    print(casa)
    Casa().Superficie()
  def Superficie(self):
    total = 0
    for i in range(len(orientaciones)):
      total += casa[orientaciones[i]]['ventanas']['superficie']
    print('Superficie acristalada: ' + str(total))
  def ParedCortina(self, orientacion, tamaño):
    casa[orientacion]['ventanas']['superficie'] += tamaño
    print(casa)
  def ComprobarProteccion(self, orientacion):
    if casa[orientacion]['ventanas']['proteccion'] != '':
      print('Protección en regla.')
    else:
      print('Protección obligatoria no presente.')
    
   
  
# Casa().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE']) <-- Esto pal main
# Casa().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE']) <--
# Casa().ParedCortina('NORTE', 4) <--
# Casa().Superficie() <--
# Casa().ComprobarProteccion('NORTE') <--