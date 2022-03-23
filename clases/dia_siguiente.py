class empresa:
    def __init__(self, nombre):
        self.nombre = nombre

class ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __del__(self):
        print("La ciudad "+str(self.nombre)+" ha sido destruida.")

class empleado:
    def __init__(self, nombre, edificio):
        self.nombre = nombre
        self.edificio = edificio

class edificio:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

Nueva_York = ciudad("Nueva_York")
Los_Angeles = ciudad("Los_Angeles")
A = edificio("A", Nueva_York)
B = edificio("B", Nueva_York)
C = edificio("C", Los_Angeles)
Martin = empleado("Martin", A)
Xing = empleado("Xing", B)
Salim = empleado("Salim", C)