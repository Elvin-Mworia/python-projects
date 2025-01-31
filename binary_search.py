def binary_search(ordered_list,term):
    size_of_list=len(ordered_list)-1

    index_of_first_element=0
    index_of_last_element=size_of_list

    while index_of_first_element<=index_of_last_element:
        mid_point=(index_of_last_element+index_of_first_element)//2

        if(ordered_list[mid_point]==term):
            return mid_point
        
        if term > ordered_list[mid_point]:
            index_of_first_element=mid_point+1
        else:
            index_of_last_element=mid_point-1

    if index_of_first_element>index_of_last_element:
        return None
    
#print(binary_search([10,20,50,60,70],60))
ordered_list=[ i for i in range(0,100000)]
print(len(ordered_list))
print(binary_search(ordered_list,588))