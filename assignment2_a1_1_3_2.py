#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment2_a1_3_2

######## Your Code Below ########
def dictionary_comp():
    subject_code = ["ES2B0","ES2B1","ES2B2","ES2B3","ES2B4"]
    studentRecord = [
                     [('John',90), ('Elvis',85), ('Thomas',95), ('Isha',85), ('Ranveer',79)],
                     [('John',90), ('Elvis',85), ('Thomas',95), ('Isha',85), ('Ranveer',79)],
                     [('John',90), ('Elvis',85), ('Thomas',95), ('Isha',85), ('Ranveer',79)],
                     [('John',90), ('Elvis',85), ('Thomas',95), ('Isha',85), ('Ranveer',79)],
                     [('John',90), ('Elvis',85), ('Thomas',95), ('Isha',85), ('Ranveer',79)]
                    ]
    sYR = {subject_code:studentRecord for (subject_code,studentRecord) in zip(subject_code,studentRecord)}
    return(sYR)
print(dictionary_comp())
