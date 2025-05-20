"""
 * Crea una función que calcule el valor del parámetro perdido
 * correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
 *   el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará
 *   la cadena de texto "Invalid values".
"""
def ohm (v=None, r=None, i=None):#Indicamos que los valores son opcionales
  if isinstance(v, (int, float)) and isinstance(r, (int, float)):
    i=(v/r)
    print("{:.2f}".format(i))#Damos formato con dos decimales
  elif isinstance(r, (int, float)) and isinstance(i, (int, float)):
    v= r*i
    print("{:.2f}".format(v))
  elif isinstance(i, (int, float)) and isinstance(v, (int, float)):
    r=(v/i)
    print("{:.2f}".format(r))
  else:
    print("Invalid values")

ohm(None,8,2)

#ChatGPT

def ohms_law(V=None, R=None, I=None):
    if (V is not None and R is not None and I is not None) or (V is None and R is None and I is None):
        return "Invalid values"

    if V is None:
        if isinstance(R, (int, float)) and isinstance(I, (int, float)):
            V = I * R
            return round(V, 2)
        else:
            return "Invalid values"

    if R is None:
        if isinstance(V, (int, float)) and isinstance(I, (int, float)):
            R = V / I
            return round(R, 2)
        else:
            return "Invalid values"

    if I is None:
        if isinstance(V, (int, float)) and isinstance(R, (int, float)):
            I = V / R
            return round(I, 2)
        else:
            return "Invalid values"

    return "Invalid values"


ohms_law(40, 10)