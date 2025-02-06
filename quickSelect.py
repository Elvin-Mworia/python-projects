#selects the ith smallest or largest element in an unordered list
def quickSelect(unsorted_array,left,right,k):
    split=partition(unsorted_array,left,right)

    if split == k:
        return unsorted_array[split]
    elif split<k:
        return quickSelect(unsorted_array,split+1,right,k)
    
    else:
        return quickSelect(unsorted_array,left,split-1,k)




def partition(unsorted_array,first,last):
    return