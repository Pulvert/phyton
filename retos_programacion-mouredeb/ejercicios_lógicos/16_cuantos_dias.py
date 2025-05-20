"""
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
"""
from datetime import date
import re

def dates (date1, date2):

    pattern = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})\b'
    coincidence = re.match(pattern, date1)

    if coincidence:

        day1, month1, year1 = date1.split("/")

        day1 = int(day1)
        month1 = int(month1)
        year1 = int(year1)

        day2, month2, year2 = date2.split("/")

        day2 = int(day2)
        month2 = int(month2)
        year2 = int(year2)

        
        date1_format = date(year1,month1,day1)
        date2_format = date(year2,month2,day2)

        difference_days = (date2_format-date1_format)

        print(f"La difrencia es de {difference_days.days} días entre ambas fechas")

    else:
        print("La fecha no coincide con el formato dd/mm/yyyy.")
  

dates("11/03/1984", "03/06/2024")

# Solución Chatgpt

from datetime import datetime

def calcular_dias_entre_fechas(fecha1, fecha2):
    formato = "%d/%m/%Y"  # Definimos el formato de la fecha

    try:
        # Convertimos las cadenas de texto a objetos datetime
        fecha1_datetime = datetime.strptime(fecha1, formato)
        fecha2_datetime = datetime.strptime(fecha2, formato)
    except ValueError:
        raise ValueError("Una de las cadenas de texto no representa una fecha correcta")

    # Calculamos la diferencia absoluta en días entre las dos fechas
    diferencia = abs((fecha2_datetime - fecha1_datetime).days)
    
    return diferencia

# Ejemplos de uso:
try:
    print(calcular_dias_entre_fechas("01/06/2023", "01/06/2024"))  # Salida: 366 días (año bisiesto)
    print(calcular_dias_entre_fechas("15/03/2022", "10/03/2022"))  # Salida: 5 días
    print(calcular_dias_entre_fechas("15/03/2022", "32/03/2022"))  # Esto lanzará una excepción
except ValueError as e:
    print(e)