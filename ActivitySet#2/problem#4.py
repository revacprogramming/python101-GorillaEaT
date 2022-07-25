

def get_cs():
    a=input("Enter string")
    return(a)


def cs_to_lot(cs):
    l=[]
    a=cs.split(";")
    for i in a:
        l.append(tuple(i.split("=")))
    return l

def lot_to_cs(lot):
    a=";".join(str(x+'='+y) for x,y in lot)
    return(a)


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
