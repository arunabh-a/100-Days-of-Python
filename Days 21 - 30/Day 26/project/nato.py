# NATO Transmition Reader: Day 26
import pandas
#Loop through rows of a data frame


nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
natoDict = {row.letter:row.code for (index, row) in nato.iterrows()}

# print(natoDict)

def phonetic():
    transmition = input("Enter a word: ").upper()
    try:
        transmitionList = [natoDict[letter] for letter in transmition]
    except KeyError:
        print("Sorry, please enter a valid word.") 
        phonetic()
    else:
        print(transmitionList)

phonetic() 