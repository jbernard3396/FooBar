def Main():
    print(1, end='')  # special case to make sure commas work right in final print
    for i in range(2, 100, +1):
        if i % 15 == 0:
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
