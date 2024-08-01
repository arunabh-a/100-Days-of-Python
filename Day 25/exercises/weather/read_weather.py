import pandas

data = pandas.read_csv('weather_data.csv')

# Data in Column

tempData = data.temp

print(tempData.mean())
print(tempData.max())

# Data in Row

print(data[data.day == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)

# Dataframe from scratch

tempDict = {
    "students" : ['Arunabh', 'Adarsh', 'Aparimey'],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(tempDict)
data.to_csv('created_dataframe.csv')