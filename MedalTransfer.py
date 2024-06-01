import numpy as np
import csv

a = "invies/2024-02-10_yale_invitational_c.csv" # name of invitational csv
b = "teams/bruh.csv" # name of team csv for invitational
oneteam = True # set to true if there's only one bxsci team competing
team1name = "Bronx High School of Science A"
team2name = "Bronx High School of Science B"
team3name = "Bronx High School of Science C"

with open(a, 'r') as f:
    reader = csv.reader(f)
    d = list(reader)

draw = np.array(d)
drawtrans = draw.transpose()
notanevent = {"number", "school", "team", "exhibition", "city", "state", "track", "rank", "total", "overall"}
drawdim = draw.shape
rows, columns = drawdim

events = {""}
eventbool = True
for i in draw[0]:
    for j in notanevent:
        if i == j:
            eventbool = False
    if eventbool:
        events.add(i)
    eventbool = True

events.remove("")
events = sorted(events)

print(events)

for i in range(0, rows):
    for j in range(0, columns):
        if draw[i][j] == "Bronx High School of Science":
            index = i

bx = draw[index]
print(bx)




