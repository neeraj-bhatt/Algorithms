def bucket_sort(arr):
    bucket = []
    for i in range(len(arr)):
        bucket.append([])
    
    for j in arr:
        index = int(10 * j)
        bucket[index].append(j)
    
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
            
    return arr
arr = [0.42, 0.32, 0.12, 0.52, 0.67, 0.31, 0.19, 0.71]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
