###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

# Para obtener datos del usuario se usa la función input()
# La función input() recibe un mensaje que se muestra al usuario
# y devuelve el valor introducido por el usuario
nombre = input('hola!, cual es tu nombre?\n')
print(f'hola! {nombre}, bienvenido')

# Ten en cuenta que la función input() devuelve un string
# Así que si queremos obtener un número se debe convertir el string a un número
age = int(input('tu edad?\n'))
print(f'tu edad va a ser {age + 3}')

# La función input() también puede devolver múltiples valores
# Para hacerlo, el usuario debe separar los valores con una coma
print("Obtener múltiples valores a la vez")
ciudad, pais = input('escribe la ciudad y luego el pais: \n').split()

# country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {ciudad}, {pais}")