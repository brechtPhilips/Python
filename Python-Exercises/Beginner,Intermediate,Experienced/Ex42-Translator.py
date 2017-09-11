#Create a simple translator
#Option catch the error if the word doens't exist
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def Translation(word):
    try:
        print(d[word.lower()])
    except KeyError:
        print("We couldn't find the word")



Translation(input("Enter a word: "))