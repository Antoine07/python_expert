fileName = './temperatures_january.txt'
cleaned = {}

def average(data, precision = 2):
    try:
        return round( sum(data)/ len(data), precision)
    except ZeroDivisionError:
        return "Aucun élément dans la liste"

try:
    with open(fileName, 'r') as file:
        # enumerate crée un compteur qui part de 0
        for i, line in enumerate(file):
            try:
                cleaned[i + 1] = float(line.strip())
            except ValueError:
                print("Line ignorée", line.strip())
except FileNotFoundError:
    print("Fichier introuvable:", fileName)
    
print(cleaned)

print(average([11, 12, 13]))
print(average([]))

# moyenne, min, max, Nombre de jour en dessous de zéro
average_temp = average(cleaned.values()) # prends dans le dictionnaire les valeurs du dictionnaire
print(average_temp)
min_temp = min(cleaned.values())
max_temp = max(cleaned.values())

print([1 for day in cleaned if cleaned[day] < 0 ])
print(sum([1 for day in cleaned if cleaned[day] < 0 ]))

# On peut faire l'économie des crochets pour calculer la somme des valeurs avec les compréhensions de liste
# dans la sum
print(sum(1 for day in cleaned if cleaned[day] < 0))

print(sum(1 for day in cleaned if cleaned[day] > average_temp))

stat = {
    'average_temp' : average_temp,
    'min' : min_temp,
    'max' : max_temp,
    'number_day_inf_zero' : sum(1 for day in cleaned if cleaned[day] < 0),
    'number_day_sup_average' : sum(1 for day in cleaned if cleaned[day] > average_temp)
}

print(stat)
