
def add(a, b):
    c=a+b
    return c


def output(a, b, sum):
    print("{0}+{1}={2}".format(a,b,sum))


def main():
    a, b = [int(x) for x in input("input?:").split()]
    sum = add(a, b)
    output(a, b, sum)


if __name__ == '__main__':
    main()
