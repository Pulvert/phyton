"""
 * ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
 """

good = {
     "Pelosos": 1,
     "Sureños_buenos": 2,
     "Enanos": 3,
     "Numeróreanos": 4,
     "Elfos": 5
 }

bad = {
     "Sureños_malos": 1,
     "Orcos": 2,
     "Goblins": 3,
     "Huargos": 4,
     "Trolls": 5
 }


def battle(army1: dict, army2: dict)->str:
  tot_army1=0
  tot_army2=0
  for x,y in army1.items():
    for z, p in good.items():
      if x == z:
        value_tot_unit = y*p
        tot_army1 += value_tot_unit
  print(tot_army1)
  for x,y in army2.items():
    for z, p in bad.items():
      if x == z:
        value_tot_unit = y*p
        tot_army2 += value_tot_unit
  print(tot_army2)

  if tot_army1 > tot_army2:
    print("Ganó el ejército del bien")
  else:
    print("Ganó el ejército del mal")

battle({"Pelosos":125,"Elfos": 50, "Enanos": 25},
 {"Orcos":75, "Trolls": 15})
