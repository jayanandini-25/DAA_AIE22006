#bubble sort
#time complexity:
#worst case:O(n^2)
#best case:O(n)
import random
import time
def bubblesort(arr):
    n=len(arr)
    swapped=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
               swapped=True
               arr[j],arr[j+1]=arr[j+1],arr[j]

    if not swapped:
       return arr
def generate_random_array(length):
    return [random.randint(0, 100) for _ in range(length)]

arr = generate_random_array(500)

start_time = time.time()*1000
sorted_arr = bubblesort(arr)
end_time = time.time()*1000

print("Bubble Sort:")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\nExecution Time:", end_time - start_time,"milliseconds")
