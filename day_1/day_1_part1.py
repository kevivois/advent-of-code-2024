f = open("input.txt","r")

data = f.readlines()
f.close

array_1 = []
array_2 = []

for line in data:
    splitted_line = line.split(" ")
    array_1.append(int(splitted_line[0]))
    array_2.append(int(splitted_line[len(splitted_line)-1]))

def fusion_sort(arr):
    if len(arr) == 2:
        return arr if arr[0] < arr[1] else [arr[1],arr[0]]
    if len(arr) == 1:
        return arr
    length = len(arr)
    first_arr = fusion_sort(arr[length//2:])
    second_arr = fusion_sort(arr[:length//2])
    result = []
    while True:
            if len(first_arr) == 0 and len(second_arr) != 0:
                 result.append(second_arr.pop(0))
            elif len(first_arr) != 0 and len(second_arr) == 0:
                 result.append(first_arr.pop(0))
            elif len(first_arr) == 0 and len(second_arr) == 0:
                 break
            else:
                if first_arr[0] <= second_arr[0]:
                    result.append(first_arr.pop(0))
                else:
                    result.append(second_arr.pop(0))
    return result

array_1 = fusion_sort(array_1)
array_2 = fusion_sort(array_2)
sm = 0
for i in range(0,len(array_1)):
     sm += abs(array_1[i] - array_2[i])
print(sm)
    



