from getopt import gnu_getopt
from re import X


class ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def catastrofe(self):
        print("La ciudad "+str(self.nombre)+" ha sido destruida.")
        for persona in empleados:
            if persona.edificio.ciudad.nombre == self.nombre:
                print(str(persona.nombre)+" ha quedado desempleado por la catastrofe.")
                print("El edificio "+str(persona.edificio.nombre)+" ha sido destruido.")


class empleado:
    def __init__(self, nombre, empresa, edificio):
        self.nombre = nombre
        self.empresa = empresa
        self.edificio = edificio

class edificio:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

ciudad1 = ciudad("Nueva York")
ciudad2 = ciudad("Los Angeles")
A = edificio("A", ciudad1)
B = edificio("B", ciudad1)
C = edificio("C", ciudad2)
e1 = empleado("Martin", "YooHoo!", A)
e2 = empleado("Xing", "YooHoo!", B)
e3 = empleado("Salim", "YooHoo!", C)
empleados = [e1, e2, e3]
estatus = {"Sedes YooHoo!":{str(ciudad1.nombre): {str(A.nombre): [str(e1.nombre), True], str(B.nombre): [str(e2.nombre), True]}, str(ciudad2.nombre): {str(C.nombre): [str(e3.nombre), True]}}}

def iniciar():
    print("Se acerca la destruccion del mundo. ¿Que ciudad caerá primero?,")
    genocidio = int(input("¿Nueva York(1) o Los Angeles(2)?: "))
    if genocidio == 1:
        ciudad1.catastrofe()
    elif genocidio == 2:
        ciudad2.catastrofe()
    else:
        print("Seleccione una opción válida")
        iniciar()

iniciar()