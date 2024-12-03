import re
f = open("input.txt","r")

data = f.read()
f.close

sm = 0
a = re.findall("mul\((\d{1,3}),(\d{1,3})\)",data)
print(a)
for reg in a:
    sm += int(reg[0])*int(reg[1])
print(sm)

       



        