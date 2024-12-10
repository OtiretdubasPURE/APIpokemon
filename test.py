import requests
import markdown

def download_poke(id :int):
    '''cette fonctoin prend en argument un id et renvoie les informations sur un pokemon'''
    
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(id))
    data = response.json()
    return data



def print_poke_stats(data):
    '''cette fonction prend en argument des donnée sur un pokemon et renvoie ses statistiques'''
    
    for statistiques in data["stats"]:
        print(f'{statistiques["stat"]["name"]}: {statistiques["base_stat"]} \n')



def premier(a :int, n :int):
    '''cette fonction renvoie les n premier pokemon de l'api depuis a'''
    
    assert a != 0, "pas de pokemon d'identifiant 0"
    
    liste = []
    for i in range(a, n):
        liste.append(download_poke(i))
    return liste




def moyenne(data):
    '''cette fonction renvoie la moyenne des pv d'une liste de pokemon en entrée'''

    somme = 0
    for pokemon in data:
        somme += pokemon['stats'][0]["base_stat"]
    return somme/len(data)

def test(texte: str):
    return markdown.markdown("texte")
