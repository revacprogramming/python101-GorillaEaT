

def get_cs():
    a=input("Enter string")
    return(a)


def cs_to_dict(cs):
    l=[]
    q={}
    a=cs.split(";")
    for i in a:
        l.append(i.split('='))
    q={x:y for x,y in l}
    return q



def dict_to_cs(d):
    a=";".join(str(x+'='+y) for x,y in d.items())
    return(a)


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
