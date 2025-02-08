import random
def quickSort(unsorted_array,first,last):
    if last-first <=0:
        return 
    else:
        partition_point=partition(unsorted_array,first,last) 
        print("pivot element {}==>{}".format(unsorted_array[partition_point],unsorted_array))
        quickSort(unsorted_array,first,partition_point-1)
        quickSort(unsorted_array,partition_point+1,last)     

def partition(unsorted_array,first_index,last_index):
    pivot=unsorted_array[first_index]#value of the pivot element
    pivot_index=first_index#index of the pivot element
    index_of_last_element=last_index#index of last element after the pivot element

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
    return less_than_pivot_index #less_than_pivot_index becomes the returned pivot element

# 100 random numbers not exceeding 100000
random_numbers = [random.randint(0, 100000) for _ in range(10)]


quickSort(random_numbers,0,len(random_numbers)-1)