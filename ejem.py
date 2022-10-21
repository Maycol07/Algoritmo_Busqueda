# Creamos una funcion de busqueda de algormitia en una lista

def busquedad_secuencial(lista, valor):

    posicion = 0
    encontrado = False

    while posicion <len(lista) and not encontrado:
        if lista[posicion] ==  valor:
            encontrado = True
        else:
                posicion += 1

    return encontrado, posicion

numeros = [2, 5, 6, 2, 1, 3, 45, 4, 34, 24]
llave = 2
print(busquedad_secuencial(numeros, llave))


llave = 5
print(busquedad_secuencial(numeros, llave))

llave = 6
print(busquedad_secuencial(numeros, llave))