import time
import math
import multiprocessing
import sys
from unittest import result

sys.set_int_max_str_digits(100000)

def factorial(num):
    print(f"factoial of {num}: ")
    result = math.factorial(num)
    print(result)
    return result

if __name__ == "__main__":
    num = [100,200,300]
    
    t = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(factorial, num)
        
    print(f"Time taken: {time.time() - t} seconds")