a=10
assert a>7, "ayagya error"
print("a is less than 10")

############################################

def avg(marks):
    assert len(marks) != 0, "List is empty and divion by 0 is not possible."
    return sum(marks)/len(marks)

mark1 = [2,3,4,5,6,7,8,9,10]
print("Average of mark1:",avg(mark1))

############################################

def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))

############################################

# initializing number
a = 4
b = 0

# using assert to check for 0
print("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print(a / b)
