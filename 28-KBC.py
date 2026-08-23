questions = [['1. Which language was used to create fb?','Python','French','Javascript','PHP','None',4],
             ['2. What is the capital of France?','Madrid','Paris','Rome','Berlin','None',2],
             ['3. Which planet is known as the Red Planet?','Venus','Jupiter','Mars','Saturn',3],
             ['4. What is 8 x 7',54,56,65,48,'None',2],
             ['5. Which animal is the largest mammal','Elephant','Giraffe','Blue whale','Polar Bear',3],
             ['6. Which language is primarily used for web page styling?','HTML','Pyhton','CSS','SQL',3]
             ]

levels = [1000,2000,3000,5000,10000,20000]
money = 0

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f'Question for Rs.{levels[i]}')
    print(f'{question[0]}')
    print(f'a. {question[1]}       b. {question[2]}')
    print(f'c. {question[3]}       d. {question[4]}')
    reply = int(input('Enter your answer(1-4):'))
    if reply == question[-1]:
        print(f'Correct answer, you have won Rs. {levels[i]}')
        if(i==4):
            money = 10000
        elif(i==9):
            money=320000
    else:
        print('Wrong answer!')
        break

print(f'Your take home money is {money}')

