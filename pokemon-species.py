import requests

def premier():
    '''cette fonction renvoie les n premier pokemon de l'api depuis a'''
    dico = {}
    for i in range(1,1025):
        data = requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(i))

        dico[data["names"][8]["name"]] = data["names"][4]["name"]
    return dico