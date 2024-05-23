def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

lista = [10, 23, 33, 45, 70, 75, 80]
objetivo = 70

indice = busqueda_binaria(lista, objetivo)

if indice != -1:
    print(f"El elemento {objetivo} se encuentra en el índice {indice}.")
else:
    print(f"El elemento {objetivo} no se encuentra en la lista.")
