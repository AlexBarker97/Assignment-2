#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A3_2

######## Your Code Below ########
class pigLatin_class(object):
    word=""
    def __init__(self, word):
        self.word = word
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    def pLatin_converter(self):
        temp = []
        wordlist = self.word.split()
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
                        if letter in self.vowels and isFirst: #first vowel
                            isFirst = 0
                            converted += letter
                        elif letter in self.vowels and not isFirst: #vowel but not first vowel
                            converted += letter
                        else: #consonant
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
                if word[0] in self.vowels:
                    OUT += converted + "hay "
                elif not isFirst:
                    OUT += converted + "ay "
                else:
                    OUT += converted[1:] + converted[0] + "way "
                temp.clear()
        return(OUT)
        
class gibberish_class(pigLatin_class): 
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    def pLatin_converter(self):
        temp = []
        wordlist = self.word.split()
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
                        if letter in gibberish_class.vowels and isFirst: #first vowel
                            isFirst = 0
                            converted += letter
                        elif letter in gibberish_class.vowels and not isFirst: #vowel but not first vowel
                            converted += letter
                        else: #consonant
                            if not isFirst:
                                converted += letter
                            else:
                                temp.append(letter)
                    elif (val <= 57 and val >= 48): #number
                        temp.append(letter)
                    else: #symbols
                        if not isFirst:
                            converted += letter
                        else:
                            temp.append(letter)
                for letter in temp:
                    converted += letter
                if word[0] in gibberish_class.vowels:
                    OUT += converted + "way "
                elif not isFirst:
                    OUT += converted + "ay "
                else:
                    OUT += converted[1:] + converted[0] + "hay "
                temp.clear()
        return(OUT)
        
test = gibberish_class("num1bers app3nded to !en2d")
print(test.pLatin_converter())