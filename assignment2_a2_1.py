#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A2_1

######## Your Code Below ########
def PigLatinImproved():
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    punc = [".",",","!",":",";","'",'"',"-","_","(",")","[","]","{","}"]
    puncFound = []
    temp = []
    IN = 1
    while IN:
        IN = input("Sentence to translate: ")
        if IN == "quit":
            IN = 0
        else:
            wordlist = IN.split()
            OUT = ""
            for word in wordlist:
                converted = ""
                if word.isdigit():
                  OUT += word + " "
                else:
                    firstLet = word[0]
                    vowelFound = 0
                    for letter in word:
                        val = ord(letter)
                        if (val <=122 and val >= 97) or (val <= 90 and val >= 65) or (val <= 57 and val >= 48):
                            if letter in vowels and not vowelFound: #first vowel
                                vowelFound = 1
                                converted += letter
                            elif letter in vowels and vowelFound: #vowel but not first vowel
                                converted += letter
                            elif letter not in vowels and (val < 48 or val > 57): #consonants
                                if vowelFound:
                                    converted += letter
                                else:
                                    temp.append(letter)
                            else: #numbers
                                if vowelFound:
                                    converted += letter
                                else:
                                    temp.append(letter)
                        elif val in punc: #punc
                            puncFound.append(letter)
                        else: #various symbols
                            temp.append(letter)
                    for letter in temp:
                        converted += letter
                    for i in puncFound:
                        converted += i
                    if firstLet in vowels:
                        OUT += converted + "hay" + " "
                    elif vowelFound:
                        OUT += converted + "ay" + " "
                    else:
                        for i in converted:
                           val=ord(i)
                           if (val <=122 and val >= 97) or (val <= 90 and val >= 65):
                               OUT += converted[1:] + converted[0] + "way" + " "
                               break
                           else:
                               OUT += converted + "way" + " "
                    converted += " "
                    puncFound.clear()
                    temp.clear()
        print(OUT)
PigLatinImproved()