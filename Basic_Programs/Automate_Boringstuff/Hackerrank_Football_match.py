import requests

url1 = "https://jsonmock.hackerrank.com/api/football_matches?year=2011&team1=Barcelona&page=1"
url2 = "https://jsonmock.hackerrank.com/api/football_matches?year=2011&team2=Barcelona&page=1"

r1 = requests.get(url1)

d1, d2 = r1.json()['data'], requests.get(url2).json()['data']

team_1_goals, team_2_goals = 0, 0
from functools import reduce
team_1_goals = reduce(lambda x,y:x+y,[int(i['team1goals']) for i in d1])
print(team_1_goals)
team_2_goals = reduce(lambda x,y:x+y,[int(i['team2goals']) for i in d1])
print(team_2_goals)

# for i in d1:
#     team_1_goals+=int(i['team1goals'])
#
# for i in d2:
#     team_2_goals+=int(i['team2goals'])
print(team_1_goals+team_2_goals)
