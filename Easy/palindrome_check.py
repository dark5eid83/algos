# Write a function that takes in a non-empty string that returns a boolean representing
# whether or not the string is a palindrome. 

# Sample input: "abcdcba"
# Sample output: True


def isPalindrome(string, i=0):
    j = len(string) - 1 - i 
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)