"""
Fichier python permettant la conversion d'un fichier Markdown en HTML.
"""

import markdown
import sys


def convert(filename: str, fichier_ou_ecrire: str):
    """
    cette fonction prend en parametre un fichier markdown 
    et crée un fichier html à partir ce ce fichier markdown.
    """
    
    
    
    with open(filename, 'r') as f :
        text = f.read()
    html = markdown.markdown(text)
    with open(fichier_ou_ecrire, 'w') as f :
        f.write(html)



if len(sys.argv) == 3:

    fichier_markdown = sys.argv[1]
    fichier_html = sys.argv[2]                 
    convert(fichier_markdown,fichier_html)



#explication: sys.argv est la liste des arguments données à l'éxecution du fichier. ressemble à ça:
#["le dossier d'où se trouve ce fichier", "fichier_markdown.md", "fichier_html.html"]

