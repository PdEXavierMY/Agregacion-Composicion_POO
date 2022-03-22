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
print("codigo destruido")
n=0
while n<10:
    print(1)
    n+=1
#>>> ?
#Yang destruido