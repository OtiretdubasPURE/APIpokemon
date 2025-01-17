"""
Ce script python crée un fichier htlm avec différentes statistiques sur un pokémon.
Prends en valeur d'entrée un nom de pokemon en Français.

ATTENTION:
Ce script à été developpé sous linux. Des problèmes ont été rencontrés quand à l'exécution
sous Windows, due à des soi-disant versions différentes de python. 

(source: un forum sur stack overflow):
"https://stackoverflow.com/questions/50401632/f-strings-giving-syntaxerror"
"""


import requests                        #importation des modules pour que le script fonctionne
from dictionnaire import dict_trad     #module pour pouvoir acceder au fichier dict_trad depuis dictionaire.py
from md_to_html import convert

#from functools import lru_cache     #Implementation d'un cache simple


#initialisation des valeurs requises pour le script.


nom_poke = str(input("entrer un nom de pokemon (avec une majuscule et en français): "))   
id = dict_trad[nom_poke]
nom_fichier = nom_poke +".md"        

#@lru_cache
def download_poke(identifiant):
    '''cette fonction prend en argument un id et renvoie les informations sur un pokemon'''

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{identifiant}")
    data = response.json()
    return data

#@lru_cache
def download_poke_trad(identifiant):
    '''
    cette fonction prend en argument un id et renvoie les informations sur un pokemon
    -pour avoir des données traduites supplémentaires
    '''

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{identifiant}")     
    #pour avoir des données cette fois traduite
    #supplémentaires
    data_trad = response.json()
    return data_trad





def output_list_md(data, data_trad, nom_fichier:str):
    """
    Cette fonction prends en paramètres des données sur un pokemon et un nom de fichier et
    crée un fichier contenant des informations sur le pokemon.
    Par exemple le type, une image ect...
    """
    
    
    with open(nom_fichier, 'w') as f:
        f.write(f"# Fiche de statistique sur le pokemon {nom_poke}\n")
        f.write(f"## {nom_poke} est de type {data["types"][0]["type"]["name"]}\n")
        f.write(f"![alt text](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png)\n")
        f.write(f"## Voici les statistiques du pokemon:\n")
        for statistiques in data["stats"]:
            f.write(f'{statistiques["stat"]["name"]}: {statistiques["base_stat"]}   \n')
        f.write(f"## Description: \n")
        f.write(f"{data_trad["flavor_text_entries"][87]["flavor_text"]} \n")
        f.write(f"{nom_poke} est un pokemon de la {data_trad["generation"]["name"]}   \n")
        #f.write(f"## Voici le cri de {nom_poke}:   \n")
        f.write(f"![Audio]({data["cries"]["latest"]})")
    return nom_fichier





#appel des fonctions:
données = download_poke(id)
print(données)
données_trad = download_poke_trad(id)
fichier_markdown = output_list_md(données, données_trad, nom_fichier) 
convert(fichier_markdown, nom_poke+".html")