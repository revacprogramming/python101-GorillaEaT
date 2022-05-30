z = 0
m = 0
y = 0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        x = line.split()
        for i in x:
            if i[0].isdigit():
                y = float(i)
                m += y
                z += 1
print(f'Average spam confidence: {m/z}')