#for calculating profit or loss
a=int(input("Cost Price- "))
b=int(input("Selling Price- "))
if a==b:
    print("No loss No profit")
elif a>b:
    print('Loss= ',a-b)
else:
    print('Profit= ',b-a)
