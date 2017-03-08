#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment2_a1_1c1

######## Your Code Below ########
def PigLatinPunc():
    VOWELS = ["a","e","i","o","u","A","E","I","O","U"]
    PuncMarks = [46,44,33,58,59,39,34,45,95,40,41,91,93,123,125]
    PuncFound = []
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
        if (val <=122 and val >= 97) or (val <= 90 and val >= 65):
            OUT = OUT + test
            continue
        elif val in PuncMarks:
            PuncFound.append(test)
            continue
        else:
            ErrorState = 1
            break
    if FirstLet in VOWELS:
        for i in PuncFound:
            OUT = OUT + i
        OUT = OUT[1:] + "hay"    
    else:
        OUT = OUT[1:L] + FirstLet
        for i in PuncFound:
            OUT = OUT + i
        OUT = OUT + "ay"
    if ErrorState == 1:
        print("Please only give letters and punctuation") 
    else:
        print(OUT)
PigLatinPunc()