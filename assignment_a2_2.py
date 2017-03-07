#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : A2_2

######## Your Code Below ########
def fibonacci(max):
    fibList = [0,1]
    x=0
    if max > 1:
        while x < max:
            L=len(fibList)
            fibList.append(fibList[L-1]+fibList[L-2])
            x=fibList[L]
        return(fibList)
    elif max == 1:
        return(fibList)
    elif max == 0:
        return([0])
    else:
        return("Fibonacci only takes positive values")
