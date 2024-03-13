n=int(input("enter a number : "))
try:
    b=7/n
    print("divsion is {b}")
except Exception as myfirstexception:
    print(myfirstexception)
else:
    print("user ny 0 nahi diya tha")
finally:
    print("is ny tu chlna he chlna hai")
