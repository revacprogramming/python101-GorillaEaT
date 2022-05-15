largest = 0
smallest = 0

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        n = float(num)
    except:
        print("Invalid input")
    if largest < n or largest == 0:
        largest = n
    if smallest > n or smallest == 0:
        smallest = n


print("Maximum number is", largest)
print("Minimum number is ", smallest)