# FizzBuzz where each function has no more than two lines of code.  Otherwise straightforward.


def Main():
    for i in range(1, 101, +1):  # find a more elegant way to get the correct range
        fizzBuzz(i)


def fizzBuzz(n):
    printNormalIfNotMultiple(n)
    printSpecialIfMultiple(n)


def printSpecialIfMultiple(n):
    if isMultipleOf3Or5(n):
        printSpecial(n)


def printSpecial(n):
    printFizzBuzzIfMultipleOf3And5(n)
    printFizzOrBuzzIfMultipleOf3or5(n)


def printFizzBuzzIfMultipleOf3And5(n):
    if isMultipleOf3And5(n):
        printTerm('FizzBuzz')


def printFizzOrBuzzIfMultipleOf3or5(n):
    printFizzIfOnlyMultipleOf3(n)
    printBuzzIfOnlyMultipleOf5(n)


def printFizzIfOnlyMultipleOf3(n):
    if isMultipleOf3(n) and not isMultipleOf3And5(n):
        printTerm('Fizz')


def printBuzzIfOnlyMultipleOf5(n):
    if isMultipleOf5(n) and not isMultipleOf3And5(n):
        printTerm('Buzz')


def printNormalIfNotMultiple(n):
    printPlainIf1(n)
    printNormalIfNot1(n)


def printNormalIfNot1(n):
    if not isMultipleOf3Or5(n) and n != 1:
        printTerm(n)


def isMultipleOf3Or5(n):
    return isMultipleOf3(n) or isMultipleOf5(n)


def isMultipleOf3And5(n):
    return isMultipleOf3(n) and isMultipleOf5(n)


def isMultipleOf3(n):
    return n % 3 == 0


def isMultipleOf5(n):
    return n % 5 == 0


def printTerm(term):
    print(', ', term,  sep='', end='')


def printPlainIf1(n):
    if n == 1:
        print(n, end='')


Main()
