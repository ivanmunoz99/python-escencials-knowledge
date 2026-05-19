###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], ['calcetin', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista1)
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5] copia la lista

# El tercer parámetro es el paso (step)
# print(lista1[desde:hasta:paso])   
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares [1, 3, 5, 7]
print(lista1[::-1]) # para devolver índices inversos [8, 7, 6, 5, 4, 3, 2, 1]


# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)


# Recuperar longitud de una lista
print("Longitud de la lista", len(lista1))
