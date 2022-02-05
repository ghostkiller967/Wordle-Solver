import requests

word_length = 5
input = [ ]

def addLetter(letter: str, position: int, exclude: bool = True, correct: bool = False):
    input.append({ "exclude": exclude, "letter": letter, "correct": correct, "position":  position })

addLetter("d", 0)
addLetter("e", 1)
addLetter("a", 2)
addLetter("t", 3, False, True)
addLetter("h", 4)

addLetter("g", 0)
addLetter("r", 1)
addLetter("i", 2, False, True)
addLetter("p", 3)
addLetter("s", 4)

with open("words.txt", "r") as f:
    text = f.read()
words = text.split('\n')
final = []
correct = []
for word in words:
    if len(word) == word_length:
        final.append(word)
for word in final:
    valid = True
    for value in input:
        if value["letter"] in word and value["exclude"]:
            valid = False
        if not value["correct"] and word[value["position"]] == value["letter"]:
            valid = False
        if value["correct"] and word[value["position"]] != value["letter"]:
            valid = False
        if not value["correct"] and not value["exclude"] and not value["letter"] in word:
            valid = False
    if valid:
        correct.append(word)
print(correct)