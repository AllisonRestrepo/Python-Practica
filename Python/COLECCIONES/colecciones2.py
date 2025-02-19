#8:09 9
lista =[1,3,5,2,6,7]
lista2 = [5,2,3]
lista.append(6)
lista.insert(2,4) #primero el indice y luego el numero qeu queremos ingresar
lista.extend([3,5,4,6]) #para sumarle esta lista a la lista que tenemos
listaNueva = lista + lista2

#para confirmar si algun elemento esta en la lista 
print(2 in lista) #saldra un booleano es decir True o False

#para saber exactamente en donde esta ese elemento 
print(lista.index(3)) #nos devuelve el indice

#para saber cuantas veces esta el elemento en la lista
print(lista.count(10))

#como eliminar un elemento de la lista
lista.pop() #sin nada borra el ultimo elemento
lista.pop(3)  #se le pasa es el indice del qeu queremos eliminar, no el numero 

lista.remove(2) #para eleminir especificamente un elemento
lista.clear() #para limpiar toda la lista
lista.reverse() #para ponerla al reves
lista.sort() #para organizar los elementos de menos a mayor
lista.sort(reverse = True) #para voltear la lista tambien pero pues en orden 