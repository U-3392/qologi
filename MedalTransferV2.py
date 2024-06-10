import numpy as np
import pandas as pd
import csv
import ConflictChecker
import SciOConversion

pathfile1 = 'invies/2024-02-10_yale_invitational_c.csv' # rename comp file here
pathfile2 = 'teams/yale team raws - Sheet1.csv' # rename team file here

full_results = pd.read_csv(pathfile1)
full_team = pd.read_csv(pathfile2)

res = full_results[full_results['school'] == 'Bronx High School of Science']
res = res.transpose() # transposing to summarise statistics
res = res.drop(['team','school', 'exhibition', 'city', 'state', 'number', 'track', 'total', 'rank']) #
res = res.rename(columns = {5: 'Team A'})

restemp = res.transpose()

event_set = set()
for col in restemp.columns:
    event_set.add(col)
event_set = sorted(event_set)
event_set.insert(0, "Competitor")
print(event_set)

people_set = set()
for person in full_team.iloc[:, 0]:
    people_set.add(person)
people_set = sorted(people_set)
print(people_set)

fin_df = pd.DataFrame(columns=event_set)
fin_df['Competitor'] = people_set

for person in full_team['Competitor']: # fix this later lmaoooooo;o;o;oo;;;o;;l;
    count = 0
    for x in range[2, 5]:
        if np.isnan(person[x]) == False:
            x
        else:
            count += 1
    
    