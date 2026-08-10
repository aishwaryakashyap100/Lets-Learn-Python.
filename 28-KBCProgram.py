print('Welcome to KBC!')

question_1 = 'Q.1. Which function is used to display output in python?'
print(question_1)
option = ['a)echo()','b)display()','c)print()','d)show()']
print(option[0])
print(option[1])
print(option[2])
print(option[3])
answer = input('Enter the answer: ')
correct_answer = 'c)print()'
if answer == correct_answer:
    print('Correct answer')
    print('you have won 1,000')
else:
    print("Wrong answer")
    print("Sorry you have'nt won anything")
