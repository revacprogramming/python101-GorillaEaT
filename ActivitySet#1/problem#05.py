def computepay(hrs,rte):
    x=0
    if (hrs<40):
        x=hrs*rte
    elif(hrs>40):
        x=(40*rte)+((hrs-40)*1.5*rte)
    return x

hrs=float(input("Enter Hours:"))
rte=float(input("Enter rate:"))
p = computepay(hrs, rte)
print("Pay", p)