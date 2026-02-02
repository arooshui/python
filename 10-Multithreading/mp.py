import multiprocessing
import time
def  print_numbers():
    for i in range(5):
        print(f"number:{i}")

def print_letters():
    for i in "abcde":
        print(f"letter:{i}")

if __name__=="__main__":
    p1 = multiprocessing.Process(target=print_letters)
    p2 = multiprocessing.Process(target=print_numbers)

    t1 = time.time()

    p1.start()
    p2.start()

    finished = time.time() - t1
    print(f"finished time {finished}")