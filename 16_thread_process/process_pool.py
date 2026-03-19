from concurrent.futures import ProcessPoolExecutor
import time

def square_num(num):
    time.sleep(3)
    return f"Square of {num} is {num*num}"

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = time.time()

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(square_num, num)
        
    for r in results:
        print(r)
    print(f"Execution time: {time.time() - t} seconds")