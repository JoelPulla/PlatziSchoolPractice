"""Escope"""

# A lo que hace referencia esto es a las varibales 
# privadas y publicas

#publica 
puplic = 100

def private_variable():
    public = 200
    private = public + 20
    print(private)
    
print(puplic) #imprime 100
private_variable() #impimr public
# print(private) # no identifica la variable y da error

