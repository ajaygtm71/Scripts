"""Question 1: Given a two integer numbers return their product and  if the product
is greater than 1000, then return their sum
"""
def multi_or_sum(num1,num2):
    product = num1*num2
    if product > 1000:
        return num1+num2
    else:
        return product

result = multi_or_sum(40,30)
print("The result is:",result)

# for stash
print("Here we will learn Stash")