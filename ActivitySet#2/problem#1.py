def add(a, b):
    c=a+b
    return c


def main():
    a = int(input("Enter a number :"))
    b = int(input("Enter a number :")) 
    c = add(a, b)
    print("The sum of 1 and 2 is {}".format(c))
main()