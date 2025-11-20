print("This is an area of circle calculator!")
radius = int(input(("enter the value of radius: ")))  
pi = 3.1416

circle_area = pi * radius ** 2  
print("Circle Area is: " + str(circle_area) + " square centimeter.")

print("  ")
print("This is the expression solver for (a-b)+(a*b)")
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
result = (a-b) + (a*b)
print("The answer is: " + str(result))
print(" ")
print("Welcome to my ASCII museum")
user_input = input("Do you want to see image 1 or 2: ")

if user_input == "1":
    print(" /~\ ") 
    print("C oo ")
    print(" _( ^)")
    print("/   ~\ ")
    print("Keely ")
    print("Here is a picture of a monkey!!!")

elif user_input == "2":
    print(" /\_/\ ")
    print("( o.o ) ")
    print(" > ^ < ")
    print("Here is a picture of a cute cate!")

