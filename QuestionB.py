# The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. 
# As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

def check(s1, s2): # function to check which version string is greater
    if float(s1) > float(s2):
        print("First version string is greater")
    elif float(s1) == float(s2):
        print("Strings are equal")
    else:
        print("First version string is smaller")
    

if __name__ == "__main__":
    s1 = str(input()) # input of string 1
    s2 = str(input()) # input of string 2
    check(s1, s2)