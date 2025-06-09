import time
import random

# Algoritmos de ordenamiento
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado += izquierda[i:]
    resultado += derecha[j:]
    return resultado

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Algoritmos de búsqueda
def busqueda_lineal(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1

def busqueda_binaria(lista, x):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == x:
            return medio
        elif lista[medio] < x:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Programa principal

# Pedir tamaño de la lista
while True:
    tam = int(input("Ingrese el tamaño de la lista aleatoria: "))
    if tam > 0:
        break
    else:
        print("Debe ingresar un número mayor a cero.")


lista = random.sample(range(tam * 2), tam)
print(f"\nLista generada (primeros 10 valores): {lista[:10]} ...")

# Ordenamiento y tiempos
print("Aplicando ordenamientos...")
for sort_func in [bubble_sort, merge_sort, quick_sort]:
    copia = lista.copy()
    inicio = time.time()
    resultado = sort_func(copia)
    fin = time.time()
    print(f"{sort_func.__name__} tomó {fin - inicio:.6f} segundos.")

# Elegir tipo de búsqueda
print("\n--- Búsqueda ---")
while True:
    tipo_busqueda = input("¿Desea buscar por posición (p) o por valor (v), o para salir (s) ? ").lower()
    if tipo_busqueda == 's':
            print("Saliendo...")
            break

    elif tipo_busqueda == 'p':
        while True:
            pos = int(input(f"\nIngrese una posición (0 a {tam - 1}): "))
            if 0 <= pos < tam:
                valor = lista[pos]
                print(f"El valor en la posición {pos} es: {valor}")
                break
            else:
                print("Posición fuera de rango.")
    elif tipo_busqueda == 'v':
        valor = int(input("\nIngrese el valor a buscar: "))
    else:
        print("Opción inválida. Ingrese 'p' para posición, 'v' para valor, o 's' para salir.") 

    # Búsqueda lineal
    t1 = time.time()
    idx_lineal = busqueda_lineal(lista, valor)
    t2 = time.time()
    if idx_lineal != -1:
        print(f"Búsqueda lineal: índice {idx_lineal}, tiempo: {t2 - t1:.6f} s")
    else:
        print(f"Búsqueda lineal: el valor {valor} no fue encontrado, tiempo: {t2 - t1:.6f} s")

    # Búsqueda binaria (lista ordenada)
    lista_ordenada = sorted(lista)
    t3 = time.time()
    idx_binaria = busqueda_binaria(lista_ordenada, valor)
    t4 = time.time()
    if idx_lineal != -1:
        print(f"Búsqueda binaria: índice {idx_binaria}, tiempo: {t4 - t3:.6f} s")
    else:
        print(f"Búsqueda binaria: el valor {valor} no fue encontrado, , tiempo: {t4 - t3:.6f} s")
