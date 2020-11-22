inp = input()
min = float(inp)
li =set()

while inp != '.':
    li.add(inp)
    inp = input()


for l in li:
    if float(l) < float(min):
        min = float(l)

print(min)
