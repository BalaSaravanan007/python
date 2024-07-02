# def longestCommonPrefix(strs):
#     if not strs:
#         return ""

#     # Start with the first string in the list as the prefix
#     prefix = strs[0]

#     # Compare the prefix with each string in the list
#     for string in strs[1:]:
#         # Update the prefix by comparing with the current string
#         while not string.startswith(prefix):
#             # Shorten the prefix by one character at a time
#             prefix = prefix[:-1]
#             # If the prefix becomes empty, there is no common prefix
#             if not prefix:
#                 return ""

#     return prefix

# # Example usage:
# strs = ["flower", "ow", "flight"]
# print(longestCommonPrefix(strs))

# def isValid(s):
#     # Stack to keep track of opening brackets
#     stack = []
#     # Hash map to store the mapping of closing brackets to their corresponding opening brackets
#     bracket_map = {')': '(', '}': '{', ']': '['}

#     # Iterate through each character in the string
#     for char in s:
#         # If the character is a closing bracket
#         if char in bracket_map:
#             # Pop the topmost element from the stack if it is not empty, otherwise assign a dummy value
#             top_element = stack.pop() if stack else '#'
#             # Check if the popped element matches the corresponding opening bracket
#             if bracket_map[char] != top_element:
#                 return False
#         else:
#             # If it's an opening bracket, push it onto the stack
#             stack.append(char)

#     # If the stack is empty, all opening brackets were properly closed
#     return not stack

# # Example usage:
# s = ")[){]}])"
# print(isValid(s))  # Output: True

# s = "(]"
# print(isValid(s))  # Output: False



    
    

