f = open("input.txt","r")

data = f.readlines()
f.close


count = 0

def is_valid(arr):
    increasing = int(arr[0]) < int(arr[1])
    for i in range(1,len(arr)):
        if increasing:
            if int(arr[i-1]) >= int(arr[i]):
                return False
        else:
            if int(arr[i-1]) <= int(arr[i]):
                return False
        delta = abs(int(arr[i-1]) - int(arr[i]))
        if delta < 1 or delta > 3:
            return False 
    return True

for line in data:
    is_safe = True
    splitted = line.split(" ")
    is_line_valid = is_valid(splitted)
    if is_line_valid:
        count+=1
    else:
        for i in range(0,len(splitted)):
            new_arr = splitted.copy()
            new_arr.pop(i)
            is_line_valid = is_valid(new_arr)
            if is_line_valid:
                count+=1
                break
    if is_line_valid:
        print("Safe")
    else:
        print("Unsafe")

print(count)

        
        
