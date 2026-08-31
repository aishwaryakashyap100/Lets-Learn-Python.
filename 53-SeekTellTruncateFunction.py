with open('myfile5.txt','r')as f:
    print(type(f))
    f.seek(9)
    print(f.tell()) # Tell() Function

    data = f.read(7)
    print(data)

# Truncate() Function
with open('sample.txt','w') as f:
    f.write('Hello world!')
    f.truncate(5)

with open('sample.txt','r')as f:
    print(f.read())