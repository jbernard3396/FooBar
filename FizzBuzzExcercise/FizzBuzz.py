def Main():
    for i in range(1, 100, +1):
        if i == 1:
            print(i, end='')  # special case to make sure commas work right in final print
        elif i % 15 == 0:
            printTerm('FizzBuzz')
        elif i % 3 == 0:
            printTerm('Fizz')
        elif i % 5 == 0:
            printTerm('Buzz')
        else:
            printTerm(i)


def printTerm(term):
    print(', ', term, sep='', end='')


Main()
