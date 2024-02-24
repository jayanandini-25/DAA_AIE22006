import time
import random
#simple array sort
def generate_random_array(length):
    return [random.randint(0, 100) for _ in range(length)]

a1 = generate_random_array(1000)

start_time = time.time()*1000
sorted_arr = a1.sort()
end_time = time.time()*1000
print("array sort:")
print(a1)
print("\nExecution Time:", end_time - start_time)
    
        

