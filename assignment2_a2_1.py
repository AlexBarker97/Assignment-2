#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A2_1

######## Your Code Below ########     
def PigLatinImproved(words):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    temp = []
    wordlist = words.split()
    OUT = ""
    for word in wordlist:
        converted = ""
        if word.isdigit():
            OUT += word + " "
        else:
            isFirst = 1
            for letter in word:
                val = ord(letter)
                if (val <=122 and val >= 97) or (val <= 90 and val >= 65): #letter
                    if letter in vowels and isFirst: #first vowel
                        isFirst = 0
                        converted += letter
                    elif letter in vowels and not isFirst: #vowel but not first vowel
                        converted += letter
                    else:
                        if not isFirst:
                            converted += letter
                        else:
                            temp.append(letter)
                else: #symbols and numbers
                    if not isFirst:
                        converted += letter
                    else:
                        temp.append(letter)
            for letter in temp:
                converted += letter
            if word[0] in vowels:
                OUT += converted + "hay "
            elif not isFirst:
                OUT += converted + "ay "
            else:
                OUT += converted[1:] + converted[0] + "way "
            temp.clear()
    return(OUT)

ExitState = 0
while not ExitState:
    IN = input("Sentence to translate: ")
    if IN == "Quit this program":
        ExitState = 1
    else:
        print(PigLatinImproved(IN))