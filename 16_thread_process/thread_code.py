import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letter():
    for i in "abcde":
        time.sleep(2)
        print(f"Letter: {i}")
        
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)        
        
t = time.time()
#start the tread
t1.start()
t2.start()

#wait for the thread to finish
t1.join()
t2.join()
print(f"Execution time: {time.time() - t} seconds")