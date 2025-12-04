expression = input("Expression: ").split(" ")


x, y, z = expression
xint = float(x)
zint = float(z)
if y == "+":
    result = (xint + zint)
   
elif y == "-":
    result = (xint - zint)
    
elif y == "*":
    result = (xint * zint)
    
elif y == "/":
    result = (xint / zint)
   
else:
    print("not a valid argument, please try again")
    exit()
print(result)