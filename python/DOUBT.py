##def roman_to_int(s):
##    # Dictionary to map Roman numerals to their integer values
##    roman_num = {
##        'I': 1,
##        'V': 5,
##        'X': 10,
##        'L': 50,
##        'C': 100,
##        'D': 500,
##        'M': 1000
##    }
##    
##    total = 0  # Initialize total to 0
##    prev_val = 0  # Initialize previous value to 0
##    
##    # Iterate over the string in reverse order
##    for i in reversed(s):
##        currentVal = roman_num[i]  # Get the integer value of the current Roman numeral character
##        
##        if currentVal < prev_val:
##            total -= currentVal  # Subtract if the current value is less than the previous value
##        else:
##            total += currentVal  # Otherwise, add the current value
##        
##        prev_val = currentVal  # Update the previous value for the next iteration
##    
##    return total  # Return the final total

strs = ["flower","flow","flight"]
for i in strs:
    print(i)


















    
