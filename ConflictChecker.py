import numpy as np
import pandas as pd
import csv
import SciOConversion

eventswith3 = ["Codebusters", "Experimental Design"] # events with 3 people

def partnerDiscrepancy(input): # finds if any event has too many or too little people
<<<<<<< HEAD
    return 2
    if input[0][0] == 'Competitors':
        
=======
    df = pd.read_csv(input)
    if len(df.index) > len(df.columns): # if rows > columns the csv is sorted by people
        df = SciOConversion.peopletoevent(df)
    
>>>>>>> 2c091ca4894d883cdf90874b88870ce58ddb6db7

def timeConflict(team, times): # checks if any person is overloaded w/ events
    return 3

def allConflicts(team, times):
    return partnerDiscrepancy(team) and timeConflict(team, times)
