class Yin: pass
class Yang:
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.o = yang
 
print(yang)
#>>> <__main__.Yang object at 0x1011da828> 
print(yang is yin.o) 
#>>> True
del(yang)
print("?")
print("codigo destruido")
n=0
while n<5:
    print(1)
    n+=1
#>>> ?
#Yang destruido

#El mensaje aparece despues de la interrogación por culpa de la variable yin.yang .