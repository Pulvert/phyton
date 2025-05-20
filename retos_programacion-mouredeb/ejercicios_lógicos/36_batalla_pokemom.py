"""
 * Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
"""

class Pokemon:
  def __init__(self, typ, atack, defense):
    self.typ = typ
    self.atack = atack
    self.defense = defense

class Effectiveness:
  effective = 2
  neutral = 1
  ineffective = 0.5


squirtle = Pokemon("water", 48, 65 )
charmander = Pokemon("fire", 52, 43)
bulbasaur = Pokemon("plant", 49, 49)
pikachu = Pokemon("electric", 55, 40)
mult = Effectiveness


def battle(pok1,pok2):

  if pok1.typ == "water" and pok2.typ == "water":
    print(50*(pok1.atack/pok2.defense)*mult.neutral)
  elif pok1.typ == "water" and pok2.typ == "fire":
    print(50*(pok1.atack/pok2.defense)*mult.effective)
  elif pok1.typ == "water" and pok2.typ == "plant":
    print(50*(pok1.atack/pok2.defense)*mult.ineffective)
  elif pok1.typ == "water" and pok2.typ == "electric":
    print(50*(pok1.atack/pok2.defense)*mult.ineffective)
  elif pok1.typ == "fire" and pok2.typ == "fire":
    print(50*(pok1.atack/pok2.defense)*mult.neutral)
  elif pok1.typ == "fire" and pok2.typ == "water":
    print(50*(pok1.atack/pok2.defense)*mult.ineffective)
  elif pok1.typ == "fire" and pok2.typ == "plant":
    print(50*(pok1.atack/pok2.defense)*mult.effective)
  elif pok1.typ == "fire" and pok2.typ == "electric":
    print(50*(pok1.atack/pok2.defense)*mult.neutral)


battle(squirtle,squirtle)

# ChatGPT

def calcular_efectividad(tipo_atacante, tipo_defensor):
    efectividad = {
        'Agua': {'Fuego': 2.0, 'Planta': 0.5, 'Eléctrico': 1.0, 'Agua': 1.0},
        'Fuego': {'Planta': 2.0, 'Agua': 0.5, 'Eléctrico': 1.0, 'Fuego': 1.0},
        'Planta': {'Agua': 2.0, 'Fuego': 0.5, 'Eléctrico': 1.0, 'Planta': 1.0},
        'Eléctrico': {'Agua': 2.0, 'Planta': 1.0, 'Fuego': 1.0, 'Eléctrico': 1.0}
    }
    return efectividad[tipo_atacante][tipo_defensor]

def calcular_dano(tipo_atacante, tipo_defensor, ataque, defensa):
    if ataque < 1 or ataque > 100 or defensa < 1 or defensa > 100:
        raise ValueError("El valor de ataque y defensa debe estar entre 1 y 100.")

    efectividad = calcular_efectividad(tipo_atacante, tipo_defensor)
    dano = 50 * (ataque / defensa) * efectividad
    return dano

# Ejemplo de uso
tipo_atacante = "Agua"
tipo_defensor = "Fuego"
ataque = 80
defensa = 70

dano = calcular_dano(tipo_atacante, tipo_defensor, ataque, defensa)
print(f"El daño del ataque es: {dano}")