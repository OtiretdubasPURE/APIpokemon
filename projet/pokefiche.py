"""
Ce script python affiche des statisques dans une fichier au format html.
Prends en valeur d'entrée un nom de pokemon (ou un id)
"""


import markdown
import requests

id = int(input("entrer un id de pokemon: "))
nom_fichier = str(input("entrer un nom pour un fichier: "))+".md"


def download_poke(identifiant :int):
    '''cette fonctoin prend en argument un id et renvoie les informations sur un pokemon'''
    
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(identifiant))
    data = response.json()
    return data

def output_list_md(data, nom_fichier:str):
    with open(nom_fichier, 'w') as f:
        f.write(f"# Fiche de statistique sur le pokemon {data["name"]}\n")
        f.write(f"## {data["name"]} est de type {data["types"][0]["type"]["name"]}\n")
        f.write(f"![alt text](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png)")
    return nom_fichier


output_list_md(download_poke(id), nom_fichier)