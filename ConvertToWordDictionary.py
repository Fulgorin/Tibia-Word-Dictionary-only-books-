
import re



#open text file in read mode
text_file = open("tokens.txt", "r", encoding="utf8")
 
#read whole file to a string
data = text_file.read()
#fix no space words
data = re.sub(r"(\w)([A-Z])", r"\1 \2", data)

#remove /n and others
singleSlash = '\\'
templist = list(data)
for c in range(len(templist)):
	if templist[c] == singleSlash[0]:
		if templist[c+1] == 'n':
			templist[c+1] = ' '

	if templist[c] == '!':
		templist[c] == ' '

	if templist[c] == '.':
		templist[c] == ' '

	if templist[c] == ',':
		templist[c] == ' '

	if templist[c] == ')':
		templist[c] == ' '

	if templist[c] == '(':
		templist[c] == ' '

	if templist[c] == '-':
		templist[c] == ' '


data = ''.join(templist)
stripped = data.replace("\n", ' ')



# keep only letters
result = re.sub('[^a-zA-Z]', ' ', stripped)

result = result.lower()


#close file
text_file.close()

#remove duplicates
def removeDuplicate(wordlist):
	return list(dict.fromkeys(wordlist))

#split

wordlist = removeDuplicate(result.split())

# sort alphabetically
sortlist = sorted(wordlist)

# write to file
with open(r'TibiaWordDictionaryOnlyBooks.txt', 'w') as fp:
    for item in sortlist:
        # write each item on a new line
        fp.write("%s\n" % item)
    

print(sortlist)

print(str(len(wordlist)) + ' Words')