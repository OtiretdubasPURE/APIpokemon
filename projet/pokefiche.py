"""
Ce script python affiche des statisques dans une fichier au format html.
Prends en valeur d'entrée un nom de pokemon (ou un id)
"""


import markdown
import requests
from dictionnaire import dict_trad

nom_poke = str(input("entrer un nom de pokemon (avec une majuscule et en français): "))
nom_fichier = nom_poke+".md"


def download_poke(nom_poke :int ,dict_trad):
    '''cette fonctoin prend en argument un id et renvoie les informations sur un pokemon'''

    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(dict_trad[nom_poke]))
    data = response.json()
    return data

def output_list_md(data, nom_fichier:str):
    with open(nom_fichier, 'w') as f:
        f.write(f"# Fiche de statistique sur le pokemon {data["name"]}\n")
        f.write(f"## {data["name"]} est de type {data["types"][0]["type"]["name"]}\n")
        f.write(f"![alt text](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png)")
    return nom_fichier


output_list_md(download_poke(id, dict_trad), nom_fichier)