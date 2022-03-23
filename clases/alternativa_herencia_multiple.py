from ast import In

class Interfaz_cristal():

  casa = {}
  orientaciones = ['NORTE', 'SUR', 'ESTE', 'OESTE']

  def Paredes(self, orientacion):
    for i in range(len(orientacion)):
      nombre = orientacion[i]
      Interfaz_cristal.casa[nombre] = {
          'ventanas': {},
      }
    print(Interfaz_cristal.casa)
    Interfaz_cristal().Ventanas([['NORTE', 0.5, ''], ['SUR', 1, ''], ['ESTE', 2, ''], ['OESTE', 1, '']])
  def Ventanas(self, ventanas):
    for i in range(len(ventanas)):
      nombre = ventanas[i][0]
      Interfaz_cristal.casa[nombre]['ventanas'] = {
        'superficie': ventanas[i][1],
        'proteccion': ventanas[i][2]
      }
    print(Interfaz_cristal.casa)
    Interfaz_cristal().Superficie()
  def Superficie(self):
    total = 0
    for i in range(len(Interfaz_cristal.orientaciones)):
      total += Interfaz_cristal.casa[Interfaz_cristal.orientaciones[i]]['ventanas']['superficie']
    print('Superficie acristalada: ' + str(total))
  def ParedCortina(self, orientacion, tamaño):
    Interfaz_cristal.casa[orientacion]['ventanas']['superficie'] += tamaño
    print(Interfaz_cristal.casa)
  def ComprobarProteccion(self, orientacion):
    if Interfaz_cristal.casa[orientacion]['ventanas']['proteccion'] != '':
      print('Protección en regla.')
    else:
      print('Protección obligatoria no presente.')