
try:
    with open('data.tx', 'r') as f:
        pass
except FileNotFoundError:
    print("Le fichier n'existe pas.")
    
    