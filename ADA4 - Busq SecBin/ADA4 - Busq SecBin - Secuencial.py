def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = [10, 23, 45, 70, 11, 15, 33]
objetivo = 70

indice = busqueda_secuencial(lista, objetivo)

if indice != -1:
    print(f"El elemento {objetivo} se encuentra en el índice {indice}.")
else:
    print(f"El elemento {objetivo} no se encuentra en la lista.")
