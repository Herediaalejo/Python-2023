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

print(matches)
print(len(matches))

win_matches = list(filter(lambda match: match["home_team_result"] == "Win", matches ))

win_matches_v2 = [element for element in matches if element["home_team_result"] == "Win"]

win_matches[0]["home_team"]="Argentina" # Al cambiar el atributo en una de las listas me lo cambia en los tres diccionarios
# Obtengo el mismo resultado

print(win_matches)
print(len(win_matches))

print(win_matches_v2)
print(matches)
