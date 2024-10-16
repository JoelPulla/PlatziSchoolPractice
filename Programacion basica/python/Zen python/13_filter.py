"""Filter """

#Nos sirve para filtrar elementos en una lista

# filter: Una función que se ejecutara para cada elemento iterable : 
# si cumple la condicion se considera para la nueva lista si no no.     

numbers = [1,2,3,4,5,6,7,8,9]
                                #condicion   #lista en la cual itera
filter1 = list(filter( lambda x: x % 2 == 0, numbers))
# print(filter1)

# ==============> Filter en diccionarios <==========

#recupera solo los que ganaron
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

wins_games = list(filter(lambda game: game['home_team_result'] == 'Win', matches))

print(wins_games)



#Ejercicio  ============> imprime solo las palabras mayores a 4<==============

def filter_by_length(words):
   # Escribe tu solución 👇
    wors_result = list(filter(lambda x: len(x) >= 4 , words))
    return wors_result

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)