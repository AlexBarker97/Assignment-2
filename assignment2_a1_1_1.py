#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment2_a1_1

######## Your Code Below ########
vowels = ["a","e","i","o","u","A","E","I","O","U"]
ExitState = 0
while not ExitState:
    OUT = ""
    ErrorState = 0
    vowelFound = 0
    word = input("Word to convert: ")
    if word == "exit":
        ExitState = 1
    for letter in word:
        val = ord(letter)
        if (val <=122 and val >= 97) or (val <= 90 and val >= 65):
            OUT += letter
        else:
            ErrorState = 1
    if word[0] in vowels:
        OUT = word + "hay"
    else:
        OUT = OUT[1:] + word[0] + "ay"
    if word == "exit":
        ExitState = 1
    if ErrorState:
        print("Please only give letters, no numbers or symbols") 
    elif not ExitState:
        print(OUT)