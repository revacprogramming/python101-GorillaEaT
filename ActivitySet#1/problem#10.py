name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d = {}
for i in handle:
    if i.startswith("From "):
        x = i.split()
        if x[1] in d:
            d[x[1]] += 1
        else:
            d[x[1]] = 1
y = max(d, key=d.get)
o = max(d.values())
print(y, o)
