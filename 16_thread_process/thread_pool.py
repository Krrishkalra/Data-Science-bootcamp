from concurrent.futures import ThreadPoolExecutor
import time

def print_num(num):
    time.sleep(1)
    return f"Number: {num}"

num = [1, 2, 3, 4, 5]
t = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_num, num)
    
for result in results:
    print(result)
print(f"Execution time: {time.time() - t} seconds")