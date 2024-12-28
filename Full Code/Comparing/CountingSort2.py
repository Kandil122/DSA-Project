
def countingSort2(A):
    n=len(A)
    comparisonNumber=0
    if n==0:   # return null in case array is empty
        return null;

    C=[0]*(n) # create auxiliary empty array

    for index, current in enumerate(A):  #scroll through array
        count=0;
        for index2 in range(n):  #for loop to find all the inferior values to the current one
            comparisonNumber+=1
            if A[index2]<current:
                count+=1  #add one to the count
        C[index]=count  #insert count in auxuliary array 
    
    
    #eliminate ducplicate in C
    for index, current in enumerate(C):
        count=0
        for index2 in range(0,len(C)-1):
            comparisonNumber+=1
            if current==C[index2]:  #if current valuwe of C has ducplicates within its array
                C[index2]=current+count  #incrememnt value
                count+=1  #change count

    B=[0]*n  # create second auxiliary array, in order not to lose any values from A during swapping of values
    for index, current in enumerate(A):
        B[C[index]]=current  #move values to their correct postion in ascending order

    return B ,comparisonNumber #return array
                
