"""Question 3: Given a string, display only those characters which
are present at an even index number.
*********************
Orginal String is  pynative
Printing only even index chars
p
n
t
v
"""
def print_even_string_char(str):
    for x in range(0,len(str),2):
        print("index,[",x,"]",str[x])
input_str = "pynative"
print("orginal string is:",input_str)
print("even index char is:")
print_even_string_char(input_str)