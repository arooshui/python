#multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time
def print_numbers(number):
    time.sleep(2)
    return f"number:{number}"

numbers=[1,2,3,4,5,6,7,8,9,10]
with ThreadPoolExecutor(max_workers=3) as executor:
    res = executor.map(print_numbers,numbers)

for re in res:
    print(re)