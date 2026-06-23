from threading import Thread
import time

def task(name):
    print(f"Starting task {name}")
    time.sleep(2)
    print(f"Completed task {name}")

start = time.time()

print(f"start",start)

# Create threads
t1 = Thread(target=task, args=("Task-1",)) # comma in the end is important
t2 = Thread(target=task, args=("Task-2",))

# Start both threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

end = time.time()

print(f"end",end)
print(f"Total time: {end - start:.2f} second")