class Yin: pass
class Yang:
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang
 
print(yang)
#>>> <__main__.Yang object at 0x1011da828> 
print(yang is yin.yang) 
#>>> True
del(yang)
print("?")
print("codigo destruido(porque no ejecuta??)")
#>>> ?
#Yang destruido

#El mensaje aparece despues de la interrogación por culpa de la variable yin.yang
#Esta variable traspasa los metodos de la clase yin(el pass) a la clase yang (yin.atributo = yang . En este caso yin.yang = yang)
#Por culpa de la clase yin, las funciones de la clase yang no se ejecutan hasta el final del codigo(por el pass)
#Es por esto que "Yang destruido" aparece al final del todo sin importar que programes, pero aparece en el orden correcto al eliminar el yin.yang


yin.yang = None
print(yang)
#>>> <__main__.Yang object at 0x1011da828> 
print(yang is yin.yang) 
#>>> True
del(yang)
print("?")
print("codigo destruido, ahora en el orden correcto")
n=0
while n<5:
    print(1)
    n+=1
#>>> ?
#Yang destruido