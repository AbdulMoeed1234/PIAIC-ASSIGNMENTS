num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

print("\nChoose the below option:")
print("1 -addition")
print("2 -subtract")
print("3 -multiply")
print("4 -divide")

x = input("Enter your choice: ")

#

if x == "1":
    print(num1+num2)
    
if x == "2":
    print(num1-num2)
    
if x == "3":
    print(num1*num2)
    
if x == "4" and num2 !=0:
    print(num1/num2)
    
else:
    print("option is not available yet")