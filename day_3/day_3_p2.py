import re
f = open("input.txt","r")

data = f.read()
f.close

sm = 0
a = re.finditer("mul\((\d{1,3}),(\d{1,3})\)",data)
# don't t'ond
# do od
for dtt in a:
    d = "do"
    dt = "don't"
    idx = dtt.span()[0]
    spans = data[:idx]
    spans = spans[::-1]
    i1 = spans.find(d[::-1])
    i2 = spans.find(dt[::-1])
    numbers = [int(dtt.group(1)),int(dtt.group(2))]
    if i1 == -1 and i2 == -1 or (i1 < i2):
        sm += numbers[0]*numbers[1]
print(sm)










       



        