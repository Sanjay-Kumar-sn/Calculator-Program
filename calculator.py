import math

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def expo(a,b):
    return a**b
def square_root(a):
    return math.sqrt(a)
def sine(angle):
    return math.sin(math.radians(angle))
def cosin(angle):
    return math.cos(math.radians(angle))
def tang(angle):
    return math.tan(math.radians(angle))

previous=[]


while True:
    try:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exponentation")
        print("6.Square root")
        print("7.sine")
        print("8.cosine")
        print("9.tangent")
        print("10.Exit")
        print("11.previous")
        ch=int(input("Enter your choice:"))
        
        match ch:
            case 1:
                a=int(input("Enter a:"))
                b=int(input("Enter b:"))
                result=add(a,b)
                print("Addition=",result)
                previous.append(result)
            case 2:
                a=int(input("Enter a:"))
                b=int(input("Enter b:"))
                result=sub(a,b)
                print("Subtraction=",sub(a,b))
                previous.append(result)
            case 3:
                a=int(input("Enter a:"))
                b=int(input("Enter b:"))
                result=mul(a,b)
                print("Multplication=",mul(a,b))
                previous.append(result)
                
            case 4:
                a=int(input("Enter a:"))
                b=int(input("Enter b:"))
                result=div(a,b)
                print("Division=",div(a,b))
                previous.append(result)
        
            case 5:
                a=int(input("Enter a:"))
                b=int(input("Enter b:"))
                result=expo(a,b)
                print("Exponentation=",expo(a,b))
                previous.append(result)

            case 6:
                a=int(input("Enter a:"))
                result=square_root(a)
                print("Square Root=",square_root(a))
                previous.append(result)
                

            case 7:
                angle=float(input("Enter angle:"))
                result=sine(angle)
                print("Sine=",sine(angle))
                previous.append(result)
              

            case 8:
                angle=float(input("Enter angle:"))
                result=cosin(angle)
                print("Cosine=",cosin(angle))
                previous.append(result)
                

            case 9:
                angle=float(input("Enter angle:"))
                result=tang(angle)
                print("Tangent=",tang(angle))
                previous.append(result)
                
            case 10:
                print("do you want to exit:")
                op=input()
                break
            case 11:
                print("previous value=",previous)
            case _:
                print("Invalid option .....try again......")

    except ZeroDivisionError:
        print("o cant be divided")
    except ValueError:
        print("Please enter a valid integer")
    except Exception as e:
        print(e)
