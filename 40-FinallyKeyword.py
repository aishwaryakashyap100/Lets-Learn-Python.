# Finally keword is always executed

try:
    l = [1,2,3,4,5,8]
    i = int(input('Enter the index: '))
    print(l[i])
except:
    print('Some error occured')

finally:
    print('always executed')

def func1():
    try:
        l = [4,5,3,5,3]
        i = int(input('Enter the index: '))
        print(l[i])
        return 1
    except:
        print('Some error occured')
        return 0

    finally:
        print('I am always executed')
        # print('I am always executed)

x = func1()
print(x)