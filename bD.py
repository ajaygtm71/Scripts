"""
Question 9: Reverse a given number and return true if it is the same as the original number
original number 121
The original and reverse number is the same

original number 125
The original and reverse number is not same
"""
def rev_string(str):
    print("original number is ",str)
    rev = str[::-1]
    if rev == str:
        print("the original amd reverse number is same")
    else:
        print("the original amd reverse number is not same")
number = str(121)
rev_string(number)