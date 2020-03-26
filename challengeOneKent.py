def addArray(add_array, add_sum):
    string_add_sum = str(add_sum)           # making add_sum into a string
    return_array = []

    # Used to place 0's in either the array or string to make them equal length
    if len(string_add_sum) < len(add_array):
        amount_more = len(add_array) - len(string_add_sum)

        for i in range(0, amount_more):
            string_add_sum = "0" + string_add_sum

    elif len(string_add_sum) > len(add_array):
        amount_more = len(string_add_sum) - len(add_array)

        for i in range(0, amount_more):
            add_array.insert(0, 0)


    # Adding each number and placing it into the return array
    carry_num = 0
    for i in range(len(add_array) - 1, -1, -1):  # Go from the ones place in the number to the 0th position in the array
        # Add each number as well as the carry number
        add_sum = add_array[i] + int(string_add_sum[i]) + carry_num    
        carry_num = 0

        # When the numbers are greater than 10 cut off where it is 10 
        # and there is a carry out
        if add_sum > 10:    
            add_sum = add_sum % 10
            carry_num = 1
        
        return_array.insert(0, add_sum) 

        if i == 0 and carry_num == 1:   # When the number gets an extra digit 
            return_array.insert(0, 1) 


    return return_array




# ###################################################
# Testing area (uncomment if wanted to test)
# array_test = [5, 6, 7, 8]
# print(addArray(array_test, 500)) 