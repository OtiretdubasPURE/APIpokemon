"""
Ce code python, une fois executé, renvoie:
1. Des statistiques qui montrent si oui ou non la somme de la 
vie des 200 premiers pokemon on plus de vie que la somme des autres.

2.
"""

import requests
import markdown
from dictionnaire import dict_trad,dict_trad_inversé

print("Attention, prendre des nombres avec un écart trop grabd prends beaucoup de temps. (jusqu'à 30min)")
print(f" \n")
range1 = int(input("entrer un indice de pokemon. (par exemple de 1):  "))
print(f" \n")
range2 = int(input("entrer un deuxieme indice de pokemon, plus grand que le premier indice.(jusqu'à 1000):  "))

nom_fichier = str(input("Entrer un nom de fichier pour la collecte des données:  "))

def download_tous_poke(range1, range2):
    '''cette fonction prend en argument une range d'identifients de Pokémon et renvoie des données.'''

    
    données = {}
    for i in range(range1, range2):
    
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        data = response.json()
        données[i] = []
        données[i].append(data["weight"])
        données[i].append(data["height"])
    return données


def download_tous_poke_species(range1, range2, données):
    '''
    cette fonction prend en argument une range d'identifients de Pokémon et renvoie des données.
    (pokemon-species)
    '''

    for i in range(range1, range2):
    
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{i}")
        data = response.json()
        données[i].append(data["capture_rate"])
    return données


def calcul_imc(infos_poke: dict):
    """
    Cette fonction prends en argument un dictionnaire avec des informations sur le pokemon. (hauteur, poids et taux de capture)
    Elle rajoute à ce dictionnaire déjà existant l'imc de ce pokemon. (hauteur / taille²)
    """
    
   
    for i in range(range1, range2):
        imc_e = ((infos_poke[i][0]) / 10) / ((infos_poke[i][1])/10)**2
        infos_poke[i].append(imc_e)

    return infos_poke


def plus_petit_grand_imc(infos_poke):
    maxi_val = 0
    maxi = 0
    mini_val = 0
    mini = 0
    for i in range(range1, range2):
        if infos_poke[i][3] > maxi_val:
            maxi_val = infos_poke[i][3]
            maxi = i
        if infos_poke[i][3] < maxi_val:
            mini_val = infos_poke[i][3]
            mini = i

    return (maxi, maxi_val, mini, mini_val)


def output_list_md(données, nom_fichier:str):
    """
    Cette fonction prends en paramètres des données sur un pokemon et un nom de fichier et
    créer un fichier contenant des informations sur le pokemon.
    Par exemple le Type, une image ect...
    """
    
    
    with open(nom_fichier, 'w') as f:
        f.write(f"# Bonjour, cette page contient l'IMC et le taux de capture de tout les pokemon compris dans l'écart qui vous a été demandé au début. \n")
        f.write(f"### Le pokemon avec le plus grand IMC est {dict_trad_inversé[resultats_finaux[0]]} avec un IMC de {resultats_finaux[1]}. \n")
        f.write(f"### A contrario le pokemon avec le plus petit IMC est {dict_trad_inversé[resultats_finaux[2]]} avec un IMC de {resultats_finaux[3]}. \n")
        f.write(f"## Voici maintenant l'IMC ainsi que le taux de capture:   \n")
        for i in range(range1, range2):
            f.write(f"IMC de {dict_trad_inversé[i]}: {données[i][3]}.    Son taux de capture: {données[i][2]} \n")
    return nom_fichier + ".md"


def ecriture_html(filename: str, fichier_ou_ecrire: str):
    """
    cette fonction prend en parametre un fichier markdown 
    et crée un fichier html à partir ce ce fichier markdown.
    """
    
    
    
    with open(filename, 'r') as f :
        text = f.read()
    html = markdown.markdown(text)
    with open(fichier_ou_ecrire, 'w') as f :
        f.write(html)
    



#partie script:
#calculs et requetes:
données1 = download_tous_poke(range1, range2)
infos_poke = download_tous_poke_species(range1, range2, données1)
infos_poke_imc = calcul_imc(infos_poke)
resultats_finaux = plus_petit_grand_imc(infos_poke_imc)

#fichier md et html:

output_list_md()













    

