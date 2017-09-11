

def CountWords(path):
    with open(path,'r') as file:
        string = file.read()
        return len(string.split(" "))

def CountWordsWithCommas(path):
    with open(path,'r') as file:
        string = file.read()
        string = string.replace(','," ")
        return len(string.split(" "))


print(CountWords("Files/words1.txt"))
print((CountWordsWithCommas("Files/words2.txt")))