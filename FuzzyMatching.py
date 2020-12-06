from fuzzywuzzy import fuzz

word = "climbing"
match = ["Banana Bread", "Clam chowder", "Gabe colburn", "Putin", "Tarzan", "climb", "rock climbing"]

matchDict = {}
for i in range(len(match)):
    matchDict.update({match[i]:fuzz.ratio(word.lower(), match[i].lower())})

matchDict = sorted(matchDict.items(), key=lambda x: x[1], reverse=True)

sortMatchDict = []
for x,y in matchDict:
    sortMatchDict.append(x)

print(matchDict)
print(sortMatchDict)
