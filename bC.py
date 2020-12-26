"""
Question 6: Given a list of numbers, Iterate it and print only those
numbers which are divisible of 5
Given list is  [10, 20, 33, 46, 55]
Divisible of 5 in a list
10
20
55
"""
def divisiable(nlist):
    print("Given list is ",nlist)
    print("Divisible of 5 in a list")
    for x in nlist:
        if x%5 == 0:
            print(x)

list_number = [10,15,36,40,88,55,60]
divisiable(list_number)