#selection sort
#time comple-worst case:O(n^2)
#best case:O(n^2)
import time
import random
def selectionsort(arr,n):
    for i in range(n-1):
        min_index=i

        for j in range(i+1,n):
            if (arr[j]<arr[min_index]):
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]
n=500
def generate_random_array(length):
    return [random.randint(0, 100) for _ in range(length)]

arr1 = generate_random_array(500)

start_time2 = time.time()*1000
sorted_arr2 = selectionsort(arr1,n)
end_time2 = time.time()*1000

print("\nSelection Sort:")
for i in range(n):
    print(arr1[i], end = " ")
print("\nExecution Time:", end_time2 - start_time2,"milliseconds")
