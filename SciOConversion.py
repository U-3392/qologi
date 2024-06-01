import csv
import numpy as py
import pandas as pd

c = "Competitors" # name of category where people are
nonevent = ["OSIS"] # non-event columns excluding the people one

full_people = pd.read_csv('teams/yale team raws - Sheet1.csv')

def eventtopeople(input):
    people = input[input[c]]
    print(people)

eventtopeople(full_people)