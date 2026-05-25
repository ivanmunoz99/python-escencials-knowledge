###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?

# +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# ----------------------------------------------------------------------------------
# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b" # en el caso de que exista antes de una b una a quiero que la devuelvas
matches = re.findall(pattern, text)
print(matches)

# -----------------------------------------------------------------------------------
# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches)

# ----------------------------------------------------------------------------------
# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)