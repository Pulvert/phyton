"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""
pp = {"player1":0, "player2":0, "tie":0}

def options (x):

  if x == ("R","R"):
    pp["tie"] += 1
  elif x == ("R","P"):
    pp["player2"] += 1
  elif x == ("R","S"):
    pp["player1"] += 1
  elif x == ("P","R"):
    pp["player1"] += 1
  elif x == ("P","P"):
    pp["tie"] += 1
  elif x == ("P","S"):
    pp["player2"] += 1
  elif x == ("S","R"):
    pp["player2"] += 1
  elif x == ("S","P"):
    pp["player1"] += 1
  elif x == ("S","S"):
    pp["tie"] += 1

def rps (list_rps):

  a,b,c = list_rps
  x = a
  options (x)
  x = b
  options (x)
  x = c
  options (x)
  print(pp)

  for key, value in pp.items():
    if value > 1 and key != "tie":
      print(f"Resultado:{key}")
      break
    elif value > 1 and key == "tie":
      print("Resultado:tie")
      break
    else:
      print("Resultado:tie")
      break

rps([("R","P"), ("R","S"), ("P","P")])
"""
"""
#Chat GPT

def calcular_ganador(jugadas):
    pp = {"player1": 0, "player2": 0, "tie": 0}

    def options(x):
        if x == ("R", "R") or x == ("P", "P") or x == ("S", "S"):
            pp["tie"] += 1
        elif (x == ("R", "S")) or (x == ("P", "R")) or (x == ("S", "P")):
            pp["player1"] += 1
        else:
            pp["player2"] += 1

    for jugada in jugadas:
        options(jugada)

    if pp["player1"] > pp["player2"]:
        return "Player 1"
    elif pp["player2"] > pp["player1"]:
        return "Player 2"
    else:
        return "Tie"

# Ejemplo de prueba.
resultado = calcular_ganador([("R", "P"), ("R", "S"), ("P", "P")])
print(f"Resultado: {resultado}")