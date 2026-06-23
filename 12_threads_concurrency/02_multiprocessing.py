import time

def task(name):
    print(f"Search task {name}")
    time.sleep(2)
    print(f"Completed task {name}")

start = time.time()

print(f"start",start)

task("A")
task("B")

end = time.time()

print(f"end",end)


print(f"Total time: {end - start:.2f} seconds")