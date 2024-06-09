import csv
import numpy as np
import pandas as pd

c = "Competitor" # name of category where people are
nonevent = [c, "OSIS"] # non-event columns
filename1 = 'teams/yale team raws - Sheet1.csv' # file location here

full_people = pd.read_csv(filename1)

def peopletoevent(input):
    people = input[c]
    event_all = input.transpose()
    event_all = event_all.drop(nonevent)
    event_all = event_all.transpose()
    # setup done
    event_set = set()
    for col in event_all:
            event_set.update(event_all[col])
    event_set = {x for x in event_set if pd.notna(x)}
    event_set = sorted(event_set)
    # all events found
    print(event_set)
    e2p = {}
    for event in event_set:
        onlyThisEvent = event_all[event_all == event]

# add new instance variables

def eventtopeople(input):
    people = input[c]
    event_all = input.transpose()
    event_all = event_all.drop(nonevent)
    event_all = event_all.transpose()

eventtopeople(full_people)