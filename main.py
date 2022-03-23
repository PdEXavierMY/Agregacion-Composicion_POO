from clases.dia_siguiente import iniciar
from clases.alternativa_herencia_multiple import *

def ejercicios():
    n = int(input("¿Qué ejercicio quieres ejecutar(1, 2 o 3)?: "))
    if n == 1:
        iniciar()
    elif n == 2:
        from clases import inmortal
    elif n == 3:
        Interfaz_cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
        Interfaz_cristal().Paredes(['NORTE', 'SUR', 'ESTE', 'OESTE'])
        Interfaz_cristal().ParedCortina('NORTE', 10)
        Interfaz_cristal().Superficie()
        Interfaz_cristal().ComprobarProteccion('NORTE')
    else:
        print("Seleccione un número permitido")
        ejercicios()

if __name__ == "__main__":
    ejercicios()