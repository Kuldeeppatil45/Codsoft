print("*-*-*-*-*- Calculator -*-*-*-*-*-")

while True:
    print("-------------------")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multplication")
    print("4.Division")
    print("5.Floor Division")
    print("6.Modulus")
    print("7.Exponential")
    print("8.Exit")

    print("-------------------")
    choice=int(input("Enter Your Choice: "))

    if choice==1:
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Number: "))
        print("Processing......")
        print("Addition is",a+b)
    elif choice==2:
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Number: "))
        print("Processing......")
        print("Subtraction is",a-b)
    elif choice==3:
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Number: "))
        print("Processing......")
        print("Multiplication is",a*b)
    elif choice==4:
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Number: "))
        print("Processing......")
        if b==0:
            print("Cannot Divide by Zero")
        else:
            print("Divison is",a/b)
    elif choice==5:
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Number: "))
        print("Processing......")
        if b==0:
            print("Cannot Divide by Zero")
        else:
            result=a//b
            print("Floor Division is",int(result))
    elif choice==6:
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Number: "))
        print("Processing......")
        print("Modulus is",a%b)
    elif choice==7:
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Number: "))
        print("Processing......")
        print("Exponential is",a**b)
    elif choice==8:
        break
    else:
        print("Invalid Input!")
print("Goodbye 👋👋")
