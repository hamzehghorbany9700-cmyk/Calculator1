def add(x,y):
  return (x + y)

def subtract(x,y):
  return (x-y)

def multiply (x,y):
  return (x*y)

def divide (x,y):
  if y==0:
    return ("Error! Division by zero!")
  else:
    return (x/y)

while 1:
	print()	
	x= float(input("please enter the first number: ",))
	y= float(input("please enter the second number: ",))

	print("Select operation:")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")


	choice = input("Enter choice (1/2/3/4): ")                  


	if choice == "1":
	    print(x, "+", y, "=", add(x, y))
	elif choice == "2":
	    print(x, "-", y, "=", subtract(x, y))
	elif choice == "3":
	    print(x, "*", y, "=", multiply(x, y))
	elif choice == "4":
	    print(x, "/", y, "=", divide(x, y))
	else:
	    print("Invalid Input")
	
	print()

	z = input("Do you want to continue? (y/n): ").lower().strip()
  if z == "n":
    break
  
