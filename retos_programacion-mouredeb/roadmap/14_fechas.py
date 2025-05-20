"""
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""
import datetime

# Fecha actual con formato solicitado
now = datetime.datetime.now()
print(f"{now.day}-{now.month}-{now.year}, {now.hour}:{now.minute}:{now.second}")

# Fecha de nacimiento con formato solicitado
birthday = datetime.datetime(1984, 3, 11, 12,10,15)
print(f"{birthday.day}-{birthday.month}-{birthday.year}, {birthday.hour}:{birthday.minute}:{birthday.second}")

# Años transcurridos
print(str(now.year-birthday.year) + " años")

# Extra

# Fecha de nacimiento Día, mes y año
print(f"{birthday.day}-{birthday.month}-{birthday.year}")
# Fecha de nacimiento Hora, minuto y segundo
print(f"{birthday.hour}:{birthday.minute}:{birthday.second}")
# Fecha de nacimiento Día de año
first_day = datetime.datetime(1984, 1, 1)
day = (birthday - first_day).days + 1
print(day)
# Fecha de nacimiento Día de la semana
week_days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
print(week_days[birthday.weekday()])
# Fecha de nacimiento Nombre del mes
months =  [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
print(months[birthday.month-1])

# Solución
from datetime import datetime

"""
Ejercicio
"""

now = datetime.now()
birth_date = datetime(1987, 4, 29, 12, 0, 0)

print(now)
print(birth_date)

difference = now - birth_date
print(type(difference))

print(f"Tengo {difference.days // 365} años.")

"""
Extra
"""

# Día, mes y año
print(birth_date.strftime("%d/%m/%y"))
print(birth_date.strftime("%d/%m/%Y"))

# Horas, minutos y segundos
print(birth_date.strftime("%H:%M:%S"))

# Día del año
print(birth_date.strftime("%j"))

# Día de la semana
print(birth_date.strftime("%A"))

# Nombre del mes
print(birth_date.strftime("%h"))
print(birth_date.strftime("%B"))

# Representación por defecto del locale
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

# AM/PM
print(birth_date.strftime("%p"))