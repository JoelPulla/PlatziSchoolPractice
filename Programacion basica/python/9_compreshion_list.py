
""" Compresion List """

# Nota: si queremos minorizar el timepo creando lsitas de datos podemos hacerlo de la siguieten forma
#       por ejemplo si quiero una lista del 1 al 100 tendria que escribir una lista con todos esos datos 
        # para ese caso podemos poner una condicicon en nuestra lista

numbers = [x+1 for x in range(100)]
#print (numbers) # imprimira del 1 al 100

celcius =[(x+1)*10 for x in range(10)] #genera desde el 0 al 10
print (celcius)

farenheit = [(temp* 9/5) * 32 for temp in celcius ]
print(farenheit)

#numero pares 
pares = [x for x in range(1,100) if x%2 == 0 ] #Saber todos los pares 
print(pares)

imapres = [x for x in range(1,100) if x%2 == 1] #imapres 
print(imapres)

"""compracion con un for normal"""
# par = 0
# list1= []
# for par in range (1,100):
#     if par % 2 == 0:
#         list1.append(par)
# print(list1)