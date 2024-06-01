import numpy as np
import pandas as pd
import csv

pathfile1 = 'invies/2024-02-10_yale_invitational_c.csv' # rename comp file here
pathfile2 = 'teams/yale team raws - Sheet1.csv' # rename team file here

full_results = pd.read_csv(pathfile1)
full_team = pd.read_csv(pathfile2)

res = full_results[full_results['school'] == 'Bronx High School of Science']
res = res.transpose() # transposing to summarise statistics
res = res.drop(['team','school', 'exhibition', 'city', 'state', 'number', 'track', 'total', 'rank']) #
res = res.rename(columns = {5: 'Team A'})

print(res)