"""
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
"""
def temp (c):
    if "Cº" in c:
      li_num_celsius = c.split("Cº")
      num_celsius=int(li_num_celsius[0])*9/5+32
      print(f"{li_num_celsius[0]} grados Celsius son {num_celsius} grados Fahrenheit")
    elif "Fº" in c:
      li_num_fah = c.split("Fº")
      num_fah=(int(li_num_fah[0])-32)*0.55
      print(f"{li_num_fah[0]} grados Fahrenheit son {round(num_fah,2)} grados Celsius")
    else:
      print("error")

temp ("10Fº")