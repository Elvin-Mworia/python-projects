#variant of the binary search
#has a running time of 0(log(log(n))) hence faster than binary search with 0(log (n))
def interpolation_search(ordered_list,term):
    size_of_list=len(ordered_list)-1

    index_of_first_element=0
    index_of_last_element=size_of_list

    while index_of_first_element<=index_of_last_element:
            mid_point=round(nearest_mid(ordered_list,index_of_first_element,index_of_last_element,term))
            if mid_point>index_of_last_element or mid_point<index_of_first_element:
                  return None
            if ordered_list[mid_point]==term:
                  return mid_point
            if term>ordered_list[mid_point]:
                  index_of_first_element=mid_point+1
            else:
                  index_of_last_element=mid_point-1

    if index_of_first_element>index_of_last_element:
          return None
        


#finds the middlepoint near the search term such that it can be skewed more to the left or right
def nearest_mid(input_list,lower_bound_index,upper_bound_index,search_value):
      return lower_bound_index+((upper_bound_index-lower_bound_index)/(input_list[upper_bound_index]-input_list[lower_bound_index]))*(search_value-input_list[lower_bound_index])


ordered_list=[ i for i in range(0,1_000_000_00)]
print(len(ordered_list))
print(interpolation_search(ordered_list,58000))