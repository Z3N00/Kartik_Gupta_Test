# Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. 
# As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).


def compare(x1, x2, x3, x4): # function to compare if line overlaps or not
    flag = False 
    if(x1<=x2):
        for i in range(x1, x2+1):
            if(i==x3) or (i==x4):
                flag = True
                break

    else:
        for i in range(x2, x1-1, -1):
            if(i==x3) or (i==x4):
                flag = True
                break

    if flag:
        return "Overlap"
    else:
        return "Not"

        
    
if __name__ == "__main__":
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())
    print(compare(x1, x2, x3, x4)) # returns with the string if the lines overlaps or not