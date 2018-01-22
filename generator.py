import itertools
import csv

# Define teams
teams = ['Team 1', 'Team 2', 'Team 3', 'Team 4', 'Team 5', 'Team 6', 'Team 7','Team 8','Team 9','Team 10']

#Iterate through teams
matches = list(itertools.permutations(players, 2))

# Print matches
for team in matches :
    print("{1} vs {2}" .format(team[0],team[1]))


# Create CSV file of matches
with open('matches.csv', 'wb') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['Home Team','Away Team'])

    for row in matches:
        csv_out.writerow(row)
