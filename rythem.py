# Author: Faras Al kharusi
# date of creation: 2/26/2020
# purpose: a set of functions that help looking for words that rhythm with a given sequence.
# in order to help writing poetry.


# converts the list to dictionary then back to list because dict can't have duplicates.
def deleteDuplicates(theList):
    theList = list(dict.fromkeys(theList))
    return theList


# add unformatted poem to poetry.txt then call the function
# you will find formatted file word by word in formatted.txt
def formatFile():
    with open("formatted.txt", "wt", encoding="utf8") as formatF:
        with open("poetry.txt", "rt", encoding="utf8") as inputTxt:
            line = inputTxt.read()
            splitedWords = line.split()
            splitedWords = deleteDuplicates(splitedWords)
            for formattedWords in splitedWords:
                formatF.write(str(formattedWords) + " \n")
    formatF.close()
    inputTxt.close()
formatFile()

# return array of all of the words in the input file
def readWords():
    with open("poetry.txt", "rt" ,encoding="utf8") as inputTxt:
        line = inputTxt.read()
        splitedWords = line.split()
        inputTxt.close()
        return splitedWords


# reduce words from Diacritics. (i.e. ???????)
# takes array of words
def reduceWords(words):
    kasr = "?"
    dham = "?"
    fthah = "?"
    tanween_kasr = "?"
    skoon = "?"
    tanween_dham = "?"
    tanween_fthah = "?"
    shaddah = "?"
    reducedArray = []

    for word in words:
        word = word.replace(kasr, "")
        word = word.replace(dham, "")
        word = word.replace(fthah, "")
        word = word.replace(tanween_kasr, "")
        word = word.replace(tanween_dham, "")
        word = word.replace(tanween_fthah, "")
        word = word.replace(skoon, "")
        word = word.replace(shaddah, "")

        reducedArray.append(word)
    return reducedArray


def findWords(array, endString, mode="reduced"):
    foundArray = []
    try:
        if mode == 'nreduced':
            for word in array:
                if word.endswith(endString):
                    foundArray.append(word)
        elif mode == 'reduced':
            reducedArray = list(reduceWords(array))

            for word in reducedArray:
                if word.endswith(endString):
                    foundArray.append(word)

        else:
            print("sorry unknown mode")
            return
        print("There are ", str(len(foundArray)), "words that start with \"" + endString + "\"")
        return foundArray

    except:
        print("there was an error finding the word")

# ----MAIN-----#
words = readWords()
# print(words)
found = findWords(words, endString="ل", mode="reduced")
print(found)
