arr = []
temp_arr = []
size = int(input())
 
 
for j in range(size):
    arr.extend(list(map(int,input().strip(" ").split(" "))))
    temp_arr.append([0]*size)
    
arr.sort()
arr.append(arr[-1])
temp = size
mat_size = size
index = 0
state = 1
roun = 1
#for j in arr:
i = 0
while (i < size*size):
        j = arr[i]
        
    
        if(state == 1):
            
            if (temp > 0):
                temp -= 1
                ghi = temp_arr[index]
                
                ghi[ghi.index(0)] = j
                temp_arr[index] = ghi
            else:
                state = 2
                temp = mat_size - 1
 
        if (state == 2):
            index += 1
            if (temp > 1):
                temp -= 1
                ghi = temp_arr[index]
                ghi = ghi[::-1]
                ghi[ghi.index(0)] = j
                temp_arr[index] = ghi[::-1]
            else:
                state = 3
                temp = mat_size
 
        if (state == 3):
            #print ("state - 3")
            if (temp > 0):
                temp -= 1
                ghi = temp_arr[index]
                ghi = ghi[::-1]
                ghi[ghi.index(0)] = j
                temp_arr[index] = ghi[::-1]
            else:
                state = 4
                temp = mat_size - 2
 
        if(state == 4):
            index -= 1
            if (temp > 0):
                temp -= 1
                val_k = temp_arr[index]
                val_k[val_k.index(0)] = j
                temp_arr[index] = val_k
            else:
                state = 1
                index = index + 1
                roun += 1
                temp = mat_size - 2
                mat_size -= 2
                continue
        i+=1
for j in range(size):
    print (" ".join(list(map(str ,temp_arr[j]))))