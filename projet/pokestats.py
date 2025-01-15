"""
Ce code python, une fois executé, renvoie:
1. Des statistiques qui montrent si oui ou non la somme de la 
vie des 200 premiers pokemon on plus de vie que la somme des autres.

2.
"""


import requests
import markdown
from dictionnaire import dict_trad,dict_trad_inversé

def download_tous_poke(identifiant):
    '''cette fonction prend en argument une range d'identifients de Pokémon et renvoie des données.'''

    données = {}
    
    for i in range(1,1000):
    
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{identifiant}")
        data = response.json()
        données[dict_trad_inversé[i]]

    

