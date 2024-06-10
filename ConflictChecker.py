import numpy as np
import pandas as pd
import csv

eventswith3 = ["Codebusters", "Experimental Design"] # events with 3 people

def partnerDiscrepancy(input): # finds if any event has too many or too little people
    return 2
    if input[0][0] == 'Competitors':
        

def timeConflict(team, times): # checks if any person is overloaded w/ events
    return 3

def allConflicts(team, times):
    return partnerDiscrepancy(team) and timeConflict(team, times)
