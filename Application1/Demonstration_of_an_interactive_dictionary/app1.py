# import json
#
# data = json.load(open("data.json")) #to load the data
#
# def Translate(w):  #w is a local variable
#     return data[w]  #w is a local variable  here the dict prints the string
#
# word = input("Enter the word to get the meaning: ")
#
# print(Translate(word))


import difflib
from difflib import get_close_matches
import json
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif (len(get_close_matches(word, data.keys())) > 0):
        yn = input("Did you mean the word %s? Enter Y if yes else N if no "% get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys()) [0]]

        elif yn == "N" or yn == 'n':
            return "Sorry then we don't have that kind of word which exists  in our dictionary"
        else:
            return "Sorry we can't understand you bruh!!!"
    else:
        return("The word is not present please double check it")

word = input("Enter the word to fetch the meaning: ")


output = translate(word)
if type(output) == list: #if type is list only then it will execute one by one to remove the ugly list and make the code optimizted
    for item in output:
        print(item) #prints out every item in the list
else:
    print(output) #prints out only when the item is string
