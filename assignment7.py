#first step
name=input("Enter tour name :")
print(name)
#Second step
number=[]
number.append(int(input("Enter your first number")))
number.append(int(input("Enter your second number")))
number.append(int(input("Enter your third number")))
print(f"Hello {name} lets explore your favourite numbes")
#third step
even_odd = []
for num in number :
    if num % 2 == 0:
        even_odd.append((num,"even"))
    else:
        even_odd.append((num,"odd"))
for evenodd in even_odd:
    print(f"\nthe number is {evenodd}")
#fourth step
print(f"Here are your number than square")
for num in number :
    square = num * num
    print(f"square of {num} is : {square}")
#fifth square
sum = number[0] + number[1] + number[2]
print(f"\n the sum of three favourite number is :{sum}")
print(f"great job , {name}! number are fascinating aren't they?")
#sixth step
print(f"\nWow , {sum} is a prime number")