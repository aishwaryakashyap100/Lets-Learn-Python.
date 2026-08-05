'''Function arguments are of four types

1. Default Arguments
2. Keyword Arguments
3. Variable Length Arguments
4. Requires Arguments '''

def average(a=9,b=8):
    print('The average is ', (a+b)/2)

average(6,4)

def name(fname,mname = 'Aishwarya', lname = 'Kashyao'):
    print("Hello,", fname, mname, lname)

name("Siddhi", 'Aish')