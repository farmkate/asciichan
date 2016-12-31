#LC101ex8.py
def analyze_text(text):
    # your code here
    lowerText = text.lower()
    alphaCount = 0
    letterCount = 0
    i = 0
    while i < len(lowerText):
        if lowerText[i].isalpha():
            alphaCount = alphaCount + 1
            if lowerText[i] == 'e':
                letterCount = letterCount + 1
        i = i + 1
    average = str(letterCount / alphaCount * 100)
    avgStr = "(" + average + "%)"
    result = "The text contains " + str(alphaCount) + " alphabetic characters, of which " + str(letterCount) + " " + avgStr + " are 'e'."
    return result

text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
print(analyze_text(text1))
print("Expected:", answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
print(analyze_text(text2))
print("Expected:", answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
print(analyze_text(text3))
print("Expected:", answer3)
