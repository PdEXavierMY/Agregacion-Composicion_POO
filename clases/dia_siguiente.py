from getopt import gnu_getopt
from re import X

class ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def catastrofe(self):
        print("La ciudad "+str(self.nombre)+" ha sido destruida.")
        for persona in empleados:
            name = persona.edificio.ciudad.nombre
            if name == self.nombre:
                print(str(persona.nombre)+" ha quedado desempleado por la catastrofe.")
                estatus["Sedes YooHoo!"][str(name)]["edificios"][str(persona.edificio.nombre)][0][1] = "Desempelado"
                print("El edificio "+str(persona.edificio.nombre)+" ha sido destruido.")
                estatus["Sedes YooHoo!"][str(name)]["edificios"][str(persona.edificio.nombre)][1] = False
                estatus["Sedes YooHoo!"][str(name)]["estado"] = "Destruida"
        print(estatus)


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
estatus = {"Sedes YooHoo!":{str(ciudad1.nombre): {"estado": "operativa", "edificios": {str(A.nombre): [[str(e1.nombre), "Empleado"], True], str(B.nombre): [[str(e2.nombre), "Empleado"], True]}}, str(ciudad2.nombre): {"estado": "operativa", "edificios": {str(C.nombre): [[str(e3.nombre), "Empleado"], True]}}}}

def iniciar():
    print(estatus)
    print("Se acerca la destruccion del mundo. ¿Que ciudad caerá primero?,")
    genocidio = int(input("¿Nueva York(1) o Los Angeles(2)?: "))
    c = 0
    if genocidio == 1:
        ciudad1.catastrofe()
        c = 1
    elif genocidio == 2:
        ciudad2.catastrofe()
        c = 2
    else:
        print("Seleccione una opción válida")
        iniciar()
    print("¿Quiere destruir la otra ciudad?(1 = Sí)")
    seguir = int(input("Por favor introduzca un número: "))
    if seguir == 1:
        if c == 1:
            ciudad2.catastrofe()
        elif c == 2:
            ciudad1.catastrofe()
    else:
        print("Pronto caerá todo...")