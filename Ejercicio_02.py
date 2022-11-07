'''
Tarea 2
La tarea gira en torno a la PokeAPI: https://pokeapi.co/docs/v2 utilizar la API v2 y el paquete requests de Python

Escribir un programa que tenga las siguientes opciones:

Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y 
se listan todos los pokemon respectivos.
Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y 
se listan todos los pokemons respectivos.
Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.
Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.
Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.
Nota: listar pokemons involucra: nombre, habilidad y URL de la imagen

'''
from re import M
from sys import maxunicode

import requests

def fun_pro2(urlpoke,pruebass, pokemo_222):
    pokemon=urlpoke
    resp= requests.get(pokemon)
    dato=resp.json()
    gene=dato[pruebass]
    list_g=[]
    for k in range (len(gene)):
        list_g.append(gene[k]['name'])
    print("Estas son todos/as los que existen:")
    for cont,value in enumerate (list_g,start=1):
        print(cont,"->",value)
    la_gene = input("\nIngrese el numero en el que salga su opcion , ya sea 1 o 2 o 3...):\n")
    poke_num=str(la_gene)
    pokegene=urlpoke + poke_num
    resp_g=requests.get(pokegene)
    dato_g=resp_g.json()
    nom_g=dato_g[pokemo_222]
    return nom_g



print("Listar pokemons de acuerdo a las opciones")
print("=============================")

print ("Opcion 1: Listar pokemons por generación.\n""Opción 2: Listar pokemons por forma\n""Opción 3: Listar pokemons por habilidad\n"
    "Opción 4: Listar pokemons por habitat\n""Opción 5: Listar pokemons por tipo\n") 

opcion = (input("\nElige una opcion e ingresa su número...\n"))

if opcion == "1":
    juli=fun_pro2("https://pokeapi.co/api/v2/generation/",'results',"pokemon_species")
    list_pokeg=[]
    for j in range (len(juli)):
        list_pokeg.append(juli[j]['name'])
    #print(list_pokeg)

    for i in range(len(list_pokeg)):
        habi="https://pokeapi.co/api/v2/pokemon/"+ list_pokeg[i]
        poke_h=requests.get(habi)
        dato_h=poke_h.json()
        habi_h=dato_h["abilities"]
        list_pokeh=[]
        for l in range (len(habi_h)):
            list_pokeh.append(habi_h[l]["ability"]["name"])
        habi_url=dato_h["sprites"]
        lista_url=[]
        #for po in range (len(habi_url)):
        lista_url.append(habi_url["front_default"])
        print(f"Pokemon:{list_pokeg[i]},Habilidades:{list_pokeh},URL de la imagen:{lista_url}")
        list_pokeh.pop(l)
        lista_url.pop(0)
