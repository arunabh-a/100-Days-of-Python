import pandas
#Loop through rows of a data frame


nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
natoDict = {row.letter:row.code for (index, row) in nato.iterrows()}

# print(natoDict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
transmition = input("Enter a word: ").upper()
transmitionList = [natoDict[letter] for letter in transmition]

print(transmitionList)
