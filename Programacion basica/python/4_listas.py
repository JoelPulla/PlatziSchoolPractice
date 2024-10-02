""" Varibales tipo listas"""

todo_list = ["saludar", "Limpiar", "lebantarme", "comer"]
todo_list_mix =  [254,"saludar", "Limpiar", "lebantarme", "comer", True, [2,3,6] ]  # puedo agregar datos sin restriccion

print(len(todo_list)) #catidad de datos
print(todo_list_mix[5]) #imprimir posicion espesifica
print(todo_list_mix[-1]) #imprimir posicion espesifica
print(todo_list_mix[0:-2]) #imprime una parte de las listas 

"""Metodos de las listas """

#Nota: Los metodos son funciones que nos pértimen realizar un funccion espesifica en el codigo 
#      en estas podemos encontar Len(), upercase(). etc

todo_list_mix.append("Hello nuevo campo") #agregar a la lista
print(todo_list_mix)

todo_list_mix.insert(0,"Primera posicion") #agrega un dato en una posicion espesifica 
print(todo_list_mix)

print(todo_list_mix.index("Limpiar"))#saber posicion espesifica del dato en la lista

new_list= [22,56,78,1,2,5,4,5]
print(max(new_list)) #saber el dato mayor de la lista
print(min(new_list)) #menor de la lista

del new_list[2:5] #eliminar datos de la lista
print(new_list)