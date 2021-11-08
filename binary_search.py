import random as rm
import time as time

'''Busqueda binaria'''

def naive_search(lista, objetivo):
    for i in range(len(lista)): # --> 0, 1, 2, 3....-1
        if lista[i] == objetivo:
            return i
    return -1


def binary_search(lista, objetivo, lim_inf=None, lim_sup=None):
    if lim_inf is None:
        lim_inf = 0 #Donde arranca la lista
    if lim_sup is None:
        lim_sup = len(lista)-1 #Donde termina la lista

    if lim_sup < lim_inf:
        return - 1

    punto_medio = (lim_inf + lim_sup) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return binary_search(lista, objetivo, lim_inf, punto_medio - 1) #Parte la lista
    else:
        return binary_search(lista, objetivo, punto_medio + 1, lim_sup) #Parte la lista


if __name__=='__main__':
    
    #Creamos una lista ordenada de 10 mil numeros aleatorios.

    cantidad = 10000
    conjunto_inicial  =set()

    while len(conjunto_inicial) < cantidad:
        conjunto_inicial.add(rm.randint(-3*cantidad, 3*cantidad))

    lista_ordenada = sorted(list(conjunto_inicial))

    #Medir el tiempo de naive_search()
    inicio = time.time()
    for objetivo in lista_ordenada:
        naive_search(lista_ordenada, objetivo)
    fin = time.time()
    print(f'Tiempo de Naive Search: {fin - inicio} segundos.')

    #Medir el tiempo de binary_search()
    inicio = time.time()
    for objetivo in lista_ordenada:
        binary_search(lista_ordenada, objetivo)
    fin = time.time()
    print(f'Tiempo de Binary Search: {fin - inicio} segundos.')