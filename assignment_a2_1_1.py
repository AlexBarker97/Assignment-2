#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment2_a1_1

######## Your Code Below ########
def PigLatinPunc():
    VOWELS = ["a","e","i","o","u"]
    IN = input("Word: ")
    word = IN.lower()
    FirstLet = word[0]
    L = len(word)
    ErrorState = 0
    i = 0
    OUT = ""
    if FirstLet in VOWELS:
        OUT = OUT + FirstLet
    while i < L:
        test = word[i]
        val = ord(test)
        i+=1
        if (val <=122 and val >= 97):
            OUT = OUT + test
            continue
        else:
            ErrorState = 1
            break
    if FirstLet in VOWELS:
        OUT = OUT[1:] + "hay"    
    else:
        OUT = OUT[1:L] + FirstLet
        OUT = OUT + "ay"
    if ErrorState == 1:
        print("Please only give letters and punctuation") 
    else:
        print(OUT)
PigLatinPunc()
