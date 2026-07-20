# Reverse a string without using slicing

#using a loop
'''def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("hello"))

# using two pointers

def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
        
    return "".join(chars)
print(reverse_string("hello"))'''

#using a loop with indices

def reverse_string(s):
    result = ""
    for i in range(len(s) -1, -1, -1):
        result += s[i]
    return result

print(reverse_string("hello"))