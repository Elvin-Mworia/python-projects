#selects the ith smallest or largest element in an unordered list
import random
def quickSelect(unsorted_array,left,right,k):
    split=partition(unsorted_array,left,right)

    if split == k:
        return unsorted_array[split]
    elif split < k:
        return quickSelect(unsorted_array,split+1,right,k)
    else:
        return quickSelect(unsorted_array,left,split-1,k)




def partition(unsorted_array,first_index,last_index):
    if first_index==last_index:#when the list has only one element
        return first_index
    
    pivot=unsorted_array[first_index]
    pivot_index=first_index
    index_of_last_element=last_index

    less_than_pivot_index=index_of_last_element
    greater_than_pivot_index=first_index+1

    while True:

        while unsorted_array[greater_than_pivot_index]< pivot and greater_than_pivot_index<last_index:
            greater_than_pivot_index+=1
        
        while unsorted_array[less_than_pivot_index]>pivot and less_than_pivot_index>=first_index:
            less_than_pivot_index-=1

        if greater_than_pivot_index<less_than_pivot_index:
            temp=unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index]=unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index]=temp
        else:
            break

    unsorted_array[pivot_index]=unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index]=pivot

    return less_than_pivot_index
    
# 100 random numbers not exceeding 100000
random_numbers = [random.randint(0, 100000) for _ in range(100)]


print(quickSelect(random_numbers,0,len(random_numbers)-1,50))