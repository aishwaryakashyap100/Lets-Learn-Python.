# Reading a file - 
f = open('myfile.txt','r')
text = f.read()
print(text)
f.close()

# Writing a file -
f = open('myfile2.txt','w')
f.write('Hello,world!')
f.close()

f = open('myfile3.txt','a')
f.write('Hey!')
f.close() # by this we can close the file

# instead of closing we can do this -
with open('myfile3.txt','a')as f:
    f.write('Hey I am inside with') # we can use with statement to automatically close the file