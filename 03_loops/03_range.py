###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

import os
os.system('clear')

print("\nrange():")

# Generado una secuencia de números del 0 al 9
for num in range(10): #NO CREA UNA LISTA
    print(num)

    # range(inicio, fin)
for num in range(5, 10):
    print(num)

# range(inicio, fin, paso)
for num in range(0, 1000, 5):
    print(num)

for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

for num in range(0, 444):
    print(num)


nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# seria para hacerlo cinco veces
for _ in range(5): # _ --> convencion para indicar que no va a utilizar esa variable
    print("hacer cinco veces algo")
