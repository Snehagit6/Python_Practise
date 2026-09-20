import random, operator

print
'==========================================='

def randomCalc(i, j):
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv}
    num = [1, 2, 3,4]
    num1, num2 = num[i], num[j]
    op = (list(ops.keys()))[i]
    answer = round(ops.get(op)(num1, num2), 3)
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer


def askQuestion(i):
    answer = randomCalc(i, i + 1)
    guess = float(input())
    return guess == answer, answer


def quiz(numOfQues):
    print('\nWelcome. This is a ' + str(numOfQues) + ' question math quiz.')
    print('Your answer should be correct to three decimal places.\n')
    score = 0
    for i in range(numOfQues):
        correct, ans = askQuestion(i)
        if correct:
            score += 1
            print('Correct!\n')
        else:
            print('Incorrect! The correct answer is ' + str(ans) + '\n')
    return ('Your score was {}/' + str(numOfQues)).format(score)


# Driver Code
print(quiz(3))

