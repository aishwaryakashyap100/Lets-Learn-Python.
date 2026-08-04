# Continue - This statement skips the rest of the loop statement and causes the next iteration to occur

for i in range(12):
    if i==10:
        print("Skip the iteration")
        continue
    print("5 X", i+1, "=", 5*(i+1))