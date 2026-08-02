import time
name = input("Enter your name : ")
name = name.capitalize()
present_time = time.strftime("%H:%M:%S")
present_time = int(time.strftime("%H"))
if (0<=present_time<=12):
    print("Good morning ",name, "it's time : ",present_time)
elif (12>= present_time <=4):
    print("Good Afternoon ",name, "it's time : ",present_time)
elif (4>= present_time <=8):
    print("Good evening ",name,"it's time : ", present_time)
else :
    print("Good night ",name,"it's time : ",present_time)