class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
 
print(yang) 
#>>> <__main__.Yang object at 0x1011da828> 
#>>> True 
del(yang)
print("?")
#>>> ? 
#Yang destruido