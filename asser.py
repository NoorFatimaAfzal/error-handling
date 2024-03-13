# initializing number
a = 4
b = 37

# using assert to check for 0
print("The value of a / b is : ")
try:
        print(a / b)
        print("End of program")
   
except ZeroDivisionError:  
    print("Divide by 0 error")
    print("End of program without dividing")     
else:
    raise ZeroDivisionError
#mtlb assertion ma error aya to program khatam ho jaye ga