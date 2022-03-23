class ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __del__(self):
        print("La ciudad "+str(self.nombre)+" ha sido destruida.")

class empleado:
    def __init__(self, nombre, empresa, edificio):
        self.nombre = nombre
        self.empresa = empresa
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
Martin = empleado("Martin", "YooHoo!", A)
Xing = empleado("Xing", "YooHoo!", B)
Salim = empleado("Salim", "YooHoo!", C)

estatus = {"Nueva York": True, "Los Angeles": False}