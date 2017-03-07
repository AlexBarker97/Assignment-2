#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A2_1

######## Your Code Below ########
def PigLatinImproved():
    vowels = ["a","e","i","o","u"]
    punc = [".",",","!",":",";","'",'"',"-","_","(",")","[","]","{","}"]
    puncFound = []
    temp = []
    IN = 1
    while IN:
        IN = input("Sentence to translate: ").lower()
        if IN == "quit":
            IN = 0
        else:
            wordlist = IN.split()
            print(wordlist)
            converted = ""
            for word in wordlist:
                firstLet = word[0]
                vowelFound = 0
                temp.clear()
                for letter in word:
                    val = ord(letter)
                    if (val <=122 and val >= 97):
                        if letter in vowels and not vowelFound:
                            vowelFound = 1
                            converted = converted + letter
                        elif not vowelFound:
                            temp.append(letter)
                            print(temp)
                        else:
                            converted = converted + letter
                    elif val in punc:
                        puncFound.append(letter)
                    else:
                        converted = converted + letter
                for letter in temp:
                    converted = converted + letter
                temp.clear()
                for i in puncFound:
                    converted = converted + i
                if firstLet in vowels:
                    converted = converted + "hay"
                elif firstLet not in vowels and vowelFound:
                    converted = converted + "ay"
                else:
                    converted = converted + "way"
                converted = converted + " "
        print(converted)
PigLatinImproved()
