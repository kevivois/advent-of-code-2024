f = open("input.txt","r")

data = f.readlines()
f.close

array_1 = []
array_2 = []

for line in data:
    splitted_line = line.split(" ")
    array_1.append(int(splitted_line[0]))
    array_2.append(int(splitted_line[len(splitted_line)-1]))

dct = {}

for n in array_1:
    dct[n] = 0
sm = 0
for n in array_2:
    try:
        a = dct[n]
        sm += n
    except:
        pass
print(sm)





