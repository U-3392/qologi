import numpy as np
import pandas as pd
import csv
import SciOConversion

eventswith3 = ["Codebusters", "Experimental Design"] # events with 3 people

def partnerDiscrepancy(input): # finds if any event has too many or too little people
    df = pd.read_csv(input)
    if len(df.index) > len(df.columns): # if rows > columns the csv is sorted by people
        df = SciOConversion.peopletoevent(df)
    

def timeConflict(team, times): # checks if any person is overloaded w/ events
    return 3

def allConflicts(team, times):
    return partnerDiscrepancy(team) and timeConflict(team, times)
