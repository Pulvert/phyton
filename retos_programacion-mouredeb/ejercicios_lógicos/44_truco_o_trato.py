"""
 * Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
 * o Trato" y un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 * - En caso contrario retornará un error.
"""
import random
import math

def halloween (trucotrato: str, persons: list):
  #Creamos listas de sustos y dulces (iconos representados por palabras)
  sustos=["calabaza","fantasma","calavera","araña","telaraña","murciélago"]
  dulces=["tarta","caramelo","chupachups","piruleta","galleta","chocolate","magdalena","donuts"]

  numb_let = 0
  tot_sust = 0

  if trucotrato == "truco":

    for x in range(len(persons)):
      for i in persons[x][0]: #Contamos las letras de todos los nombres
        numb_let+=1

    numb_let = numb_let/2 #Dividimos entre 2(Un susto por cada 2 letras)
    numb_let = math.floor(numb_let) #Redondeamos decimales
    tot_sust += numb_let #Sumamos al total

    numb_age=0
    for x in range(len(persons)):
      if persons[x][1] % 2 == 0: #Revisamos las edades que sean pares
        tot_sust +=2 #Sumamos dos por cada edad par

    cm_tot = 0
    for x in range(len(persons)):
      cm = persons[x][2] #Tomamos el tercer elemento de cada sublista
      b = int(cm.split("cm")[0]) #Quitamos cm y lo convertimos en número
      cm_tot+=b #Sumamos al total

    cm2 = cm_tot/100 #Dividimos entre 100
    cm3 = math.floor(cm2) #Redondeamos
    cm4 = cm3*3 #3 sustos por cada 100
    tot_sust+=cm4 #Sumamos al total

    list_sustos = []
    for x in range(tot_sust): #Del total de sustos, creamos lista random
      list_sustos.append(sustos[random.randint(0,len(sustos)-1)])

  print(list_sustos)


  numb_dul = 0

  if trucotrato == "trato": #Sería repitiendo lo anterior con la lógica solicitada
    pass

  else:
    print("error")


halloween("truco", [["Pedro",12,"150cm"],["Sandra",8,"120cm"],["Juan",9,"135cm"]])


# ChatGPT

import random

def generar_sustos(num_sustos):
    sustos = ['🎃', '👻', '💀', '🕷', '🕸', '🦇']
    return [random.choice(sustos) for _ in range(num_sustos)]

def generar_dulces(num_dulces):
    dulces = ['🍰', '🍬', '🍡', '🍭', '🍪', '🍫', '🧁', '🍩']
    return [random.choice(dulces) for _ in range(num_dulces)]

def truco_o_trato(tipo, personas):
    if tipo.lower() not in ['truco', 'trato']:
        return "Error: Tipo debe ser 'truco' o 'trato'."

    total_sustos = 0
    total_dulces = 0

    total_altura = sum(persona['altura'] for persona in personas)

    for persona in personas:
        nombre = persona['nombre']
        edad = persona['edad']
        altura = persona['altura']

        if tipo.lower() == 'truco':
            sustos = (len(nombre) // 2)
            if edad % 2 == 0:
                sustos += 2
            total_sustos += sustos
        elif tipo.lower() == 'trato':
            dulces = len(nombre)
            dulces += min(10, edad // 3)
            dulces += min(6, altura // 50) * 2
            total_dulces += dulces

    if tipo.lower() == 'truco':
        total_sustos += (total_altura // 100) * 3
        return generar_sustos(total_sustos)
    else:
        total_dulces += (total_altura // 50) * 2
        return generar_dulces(total_dulces)

# Ejemplo de uso:
personas = [
    {'nombre': 'Juan', 'edad': 8, 'altura': 120},
    {'nombre': 'Ana', 'edad': 7, 'altura': 110},
    {'nombre': 'Luis', 'edad': 10, 'altura': 130},
]

print(truco_o_trato('truco', personas))
print(truco_o_trato('trato', personas))