import threading
import time

start = time.perf_counter()

def Sleep1():
    print("I am starting [Sleep1]")
    time.sleep(1)
    print("Im finished [Sleep1]")

t1 = threading.Thread(target=Sleep1)
t2 = threading.Thread(target=Sleep1)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)}')