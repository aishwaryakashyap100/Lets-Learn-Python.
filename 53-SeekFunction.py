with open('myfile5.txt','r')as f:
    print(type(f))
    f.seek(9)

    data = f.read(7)
    print(data)