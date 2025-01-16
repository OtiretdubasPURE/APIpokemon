"""
Bienvenue sur ce fichier python.
Ce script crée une page html comprenant des données sur un intervalle de Pokemons. (de 1 à 1005)
Il calcule l'IMC de tout ces Pokemons, puis trouve ceux avec le plus grand IMC.
Enfin il affiche l'IMC de chaque pokemon ainsi que son taux de capture.

Non testé sous windows.
"""

import requests
import markdown
from dictionnaire import dict_trad_inversé


#Affichage de base du script


print("Attention, prendre des nombres avec un écart trop grabd prends beaucoup de temps. (jusqu'à 30min)")
print(f" \n")
range1 = int(input("entrer un indice de pokemon. (par exemple de 1):  "))
print(f" \n")
range2 = int(input("entrer un deuxieme indice de pokemon, plus grand que le premier indice.(jusqu'à 1000):  "))

nom_fichier = str(input("Entrer un nom de fichier pour la collecte des données:  "))




def download_tous_poke(range1: int, range2: int):
    '''cette fonction prend en argument une intervalle d'identifients de Pokémon et renvoie des données.'''

    
    données = {}
    for i in range(range1, range2):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        data = response.json()
        données[i] = []
        données[i].append(data["weight"])
        données[i].append(data["height"])
    return données


def download_tous_poke_species(range1: int, range2: int, données: dict) -> dict:
    '''
    cette fonction prend en argument une intervalle d'identifients de Pokémon et renvoie des données.
    (pokemon-species)
    '''

    for i in range(range1, range2):
    
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{i}")
        data = response.json()
        données[i].append(data["capture_rate"])
    return données


def calcul_imc(infos_poke: dict) -> dict:
    """
    Cette fonction prends en argument un dictionnaire avec des informations sur le pokemon. (hauteur, poids et taux de capture)
    Elle rajoute à ce dictionnaire déjà existant l'imc de ce pokemon. (hauteur / taille²)
    """
    
   
    for i in range(range1, range2):
        imc_e = ((infos_poke[i][0]) / 10) // ((infos_poke[i][1])/10)**2
        infos_poke[i].append(imc_e)

    return infos_poke


def plus_petit_grand_imc(infos_poke: dict) -> tuple:
    """
    Cette fonction prends en argument un dictionnaire avec des données précises sur un Pokemon et
    renvoie un tuple comme ci-dessous:
    -le nom du Pokemon avec l'IMC le plus gros et son IMC
    -le nom du Pokemon avec l'IMC le plus petit et son IMC
    """
    
    
    
    maxi_imc = 0
    maxi = 0
    mini_imc = infos_poke[0][3]
    mini = 0
    for i in range(range1, range2):
        if infos_poke[i][3] > maxi_imc:
            maxi_imc = infos_poke[i][3]
            maxi = i
        if infos_poke[i][3] < maxi_imc:
            mini_imc = infos_poke[i][3]
            mini = i

    return (maxi, maxi_imc, mini, mini_imc)







def output_list_md(données: dict, resultats: tuple, nom_fichier:str):
    """
    Cette fonction prends en paramètres des données sur une intervalle de Pokemon pour créer jun fichier html avec:
    Le Pokemon avec le plus gros IMC et de même pour le plus petit IMC
    La liste des Pokemons avec leurs IMC et leurs taux de capture.
    
    """
    nom_md = nom_fichier + ".md"
    
    with open(nom_md, 'w') as f:
        f.write(f"# Bonjour, cette page contient l'IMC et le taux de capture de tout les pokemon compris dans l'écart qui vous a été demandé au début. \n")
        f.write(f"### Le pokemon avec le plus grand IMC est {dict_trad_inversé[resultats[0]]} avec un IMC de {resultats[1]}. \n")
        f.write(f"### A contrario le pokemon avec le plus petit IMC est {dict_trad_inversé[resultats[2]]} avec un IMC de {resultats[3]}. \n")
        f.write(f"## Voici maintenant l'IMC ainsi que le taux de capture:   \n")
        for i in range(range1, range2):
            f.write(f"IMC de {dict_trad_inversé[i]}: {données[i][3]}.    Son taux de capture: {données[i][2]}   \n")
    return nom_md


def ecriture_html(filename: str, nom_fichier: str):
    """
    cette fonction prend en parametre un fichier markdown 
    et crée un fichier html à partir ce ce fichier markdown.
    """
    
    
    with open(filename, 'r') as f :
        text = f.read()
    html = markdown.markdown(text)
    with open(nom_fichier + ".html", 'w') as f :
        f.write(html)
    



#partie script:

#calculs et requetes:
données1 = download_tous_poke(range1, range2)
infos_poke = download_tous_poke_species(range1, range2, données1)
infos_poke_imc = calcul_imc(infos_poke)
resultats_finaux = plus_petit_grand_imc(infos_poke_imc)

#fichier md et html:

fichier_markdown = output_list_md(infos_poke_imc, resultats_finaux, nom_fichier)
ecriture_html(fichier_markdown, nom_fichier)













    

