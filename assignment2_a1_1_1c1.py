#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment2_a1_1c1

######## Your Code Below ########
vowels = ["a","e","i","o","u","A","E","I","O","U"]
punc = [".",",","!",":",";","'",'"',"-","_","(",")","[","]","{","}"]
ExitState = 0
while not ExitState:
    puncFound = []
    OUT = ""
    ErrorState = 0
    word = input("Word to convert: ")
    if word == "exit":
        ExitState = 1
    isFirst = 1
    for letter in word:
        val = ord(letter)
        if (val <=122 and val >= 97) or (val <= 90 and val >= 65):
            if word[0] in vowels and isFirst:
                OUT += letter
                isFirst = 0
            elif isFirst:
                puncFound.append(letter)
                isFirst = 0
            else:
                OUT += letter
        elif letter in punc:
            puncFound.append(letter)
        else:
            ErrorState = 1
    if word[0] in vowels:
        for i in puncFound:
            OUT += i
        OUT += "hay"
    else:
        for i in puncFound:
            OUT += i
        OUT += "ay"
    if word == "exit":
        ExitState = 1
    if ErrorState:
        print("Please only give letters and punctuation") 
    elif not ExitState:
        print(OUT)