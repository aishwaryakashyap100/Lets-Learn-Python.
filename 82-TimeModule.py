import time

def usingWhile():
    i = 0
    i = i+1
    while i<50000:
        i = i+1
        print(i)


def usingFor():
    for i in range(50000):
        print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time() # time.time()
usingWhile()
print(time.time() - init)
print(t1)

print(4)
time.sleep(3)
print('This is printed after 3 seconds') # time.sleep()

t = time.localtime()
formatted_time = time.strftime('%Y-%m-%d %H:%M:%S',t) # time.srtftime()

print(formatted_time)