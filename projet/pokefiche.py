"""
Ce script python crée un fichier HTML avec différentes statistiques sur un Pokémon.
Prends en valeur d'entrée un nom de pokemon en Français.

ATTENTION:
Ce script à été developpé sous linux. Des problèmes ont été rencontrés quand à l'exécution
sous Windows, due à des versions différentes de python. 

(source: stack overflow):
"https://stackoverflow.com/questions/50401632/f-strings-giving-syntaxerror"


EXECUTION DU SCRIPT:
Deux mannières possibles d'éxecuter ce script:

-de mannière classique dans l'interpréteur python: %run pokefiche.py
Le script vous demandera un nom de Pokémon.

-Sinon en executant le programme avec: python3 pokefiche.py {identifiant de votre Pokémon}

"""


import requests                                        
from dictionnaire import dict_trad, dict_trad_inversé     #module pour pouvoir acceder aux fichiers dict_trad et dict_trad_inversé depuis dictionaire.py
from md_to_html import convert
import sys                                                 #module systeme pour récuperer les données en entrée 


#initialisation des valeurs requises pour le script.


if len(sys.argv) == 2:
    id = sys.argv[1]
    nom_poke = dict_trad_inversé[int(id)]
else:
    nom_poke = str(input("entrer un nom de pokemon (avec une majuscule et en français): ")) 
    id = dict_trad[nom_poke]
nom_fichier = nom_poke +".md"  



def download_poke(identifiant):
    '''cette fonction prend en argument un id et renvoie les informations sur un pokemon'''

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{identifiant}")
    data = response.json()
    response2 = requests.get(f"{data["types"][0]["type"]["url"]}")
    data2 = response2.json()
    return data, data2

def download_poke_trad(identifiant):
    '''
    cette fonction prend en argument un id et renvoie les informations sur un pokemon
    -pour avoir des données traduites supplémentaires
    '''

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{identifiant}")
    
    data_trad = response.json()
    
    return data_trad





def poke_to_md(data: dict, data_trad: dict, data2: dict, nom_fichier:str):
    """
    Cette fonction prends en paramètres des données sur un pokemon et un nom de fichier et
    crée un fichier contenant des informations sur le pokemon.
    Par exemple le type, une image ect...
    """
    
    
    with open(nom_fichier, 'w') as f:
        f.write(f"# Fiche de statistique sur le pokemon {nom_poke}\n")
        f.write(f"## {nom_poke} est de type {data2["names"][3]["name"]}\n")
        f.write(f"![alt text](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png)\n")
        f.write(f"## Voici les statistiques du pokemon:\n")
        for statistiques in data["stats"]:
            f.write(f'{statistiques["stat"]["name"]}: {statistiques["base_stat"]}   \n')
        f.write(f"## Description: \n")
        f.write(f"{data_trad["flavor_text_entries"][87]["flavor_text"]} \n")
        f.write(f"{nom_poke} est un pokemon de la {data_trad["generation"]["name"]}   \n")
    return nom_fichier





def fiche_pokemon(id: int)-> None:
    """
    Cette fonction éxecute les fonctions dans le bon ordre pour créer un fichier markdown et HTML.
    prends en entrée un identifiant de Pokémon
    renvoie deux fichier: .md et .HTLM
    
    """

    données,données2 = download_poke(id)
    données_trad = download_poke_trad(id)
    fichier_markdown = poke_to_md(données, données_trad, données2, nom_fichier) 
    convert(fichier_markdown, nom_poke+".html")
    print(f"Fichiers créés avec succès!")


fiche_pokemon(id)  





