import csv
import numpy as np
import pandas as pd

c = "Competitor" # name of category where people are
nonevent = [c, "OSIS"] # non-event columns
filename1 = 'teams/yale team raws - Sheet1.csv' # file location here


<<<<<<< HEAD
full_people = pd.read_csv(filename1)
=======
>>>>>>> 2c091ca4894d883cdf90874b88870ce58ddb6db7
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
    # print(event_set)
    # print(event_all)
    people = sorted(people)
    e2p = {
        'Event' : event_set,
        'Competitor 1' : ['test'],
        'Competitor 2' : ['test 2'],
        'Competitor 3' : ['test 3']
    }

    print(e2p)
    print(type(e2p))
    print(pd.DataFrame.to_dict(e2p, orient='index'))

    for event in event_all:
         return 2
    
    
    print(e2p)

    for event in event_set:
<<<<<<< HEAD
        all_event_loc = {}
        event_loc = {}
        

=======
        onlyThisEvent = event_all[event_all == event]
>>>>>>> 2c091ca4894d883cdf90874b88870ce58ddb6db7

# add new instance variables

def eventtopeople(input):
    people = input[c]
    event_all = input.transpose()
    event_all = event_all.drop(nonevent)
    event_all = event_all.transpose()

peopletoevent(full_people)