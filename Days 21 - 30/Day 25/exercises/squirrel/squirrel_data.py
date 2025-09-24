# Squirrel DataFrame: Day 25
import pandas as pd

data = pd.read_csv('2018_Squirrel_Data.csv')

fur = data['Primary Fur Color']

gray = len(fur[fur == 'Gray'])
red = len(fur[fur == 'Red'])
black = len(fur[fur == 'Black'])

thisDict = {
    "Fur Color" : ["Gray", "Red", "Black"],
    "Count" : [gray, red, black]
}

df = pd.DataFrame(thisDict)
df.to_csv('squirrel_count.csv')
