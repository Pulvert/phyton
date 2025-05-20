"""
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""
import re

text = "Los mejores vinos son los de 1984"
# Busca uno o + dígitos
pattern = r"\d+"
# Los guarda en "result"
result = re.findall(pattern,text)
print(result)

# Extra

# Validar un email - contiene @ y solo hotmail.com y gmail.com

email = "dserrano@gmail.com"

pattern = r"@hotmail.com"
pattern2 = r"@gmail.com"
if pattern in email or pattern2 in email:
  print("email correcto")
else:
  print("email incorrecto")

# Validar un número de teléfono - 9 cifras

tel_num = "625587415"
pattern = r"^\d{9}$"

if re.match(pattern, tel_num):
  print("teléfono correcto")
else:
  print("teléfono incorrecto")

# Validar un url - termina en .com o .es

url = "mc.com"
pattern = r'\.com|\.es$'
if re.search(pattern, url):
  print("url correcta")
else:
  print("url incorrecta")

# Solución

import re

"""
Ejercicio
"""

def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)

print(find_numbers("Este es el ejercicio 16 publicado 15/04/2024."))


"""
Extra
"""

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))

print(validate_email("mouredev@gmail.com"))


def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))

print(validate_phone("+34 901 65 89 04"))


def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))

print(validate_url("http://www.moure.dev"))