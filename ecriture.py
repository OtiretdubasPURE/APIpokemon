import markdown


def ecr_test(filename: str, fichier_ou_ecrire: str):
    """
    cette fonction prend en parametre un fichier mardown 
    et ecris dans un fichier traduit en html
    """
    
    
    
    with open(filename, 'r') as f :
        text = f.read()
    html = markdown.markdown(text)
    with open(fichier_ou_ecrire, 'w') as f :
        f.write(html)

def output_list_md(my_list: list[str], filename: str):
    
    
    with open(filename, 'w') as f:
        f.write(f"# Test markdown python \n")
        f.write(f"## Une liste de {len(my_list)}\n")
        for i in range(1,len(my_list)+1):
            f.write(f'{i}. {my_list[i-1]}\n')

