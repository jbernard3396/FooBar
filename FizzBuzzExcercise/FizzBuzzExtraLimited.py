def Main():
    printListContents(generateFizzBuzzList(100))


def printListContents(lst):
    print(', '.join(map(str, lst)))


def generateFizzBuzzList(n):
    return [fizzBuzz(x) for x in range(1, n+1)]


def fizzBuzz(x):
    return getWord(x) if isMultipleOf3Or5(x) else x


def isMultipleOf3Or5(x):
    return isMultipleOf3(x) or isMultipleOf5(x)


def isMultipleOf3(x):
    return x % 3 == 0


def isMultipleOf5(x):
    return x % 5 == 0


def getWord(x):
    return getFizzIfMultipleOf3(x) +  getBuzzIfMultipleOf5(x)


def getFizzIfMultipleOf3(x):
    return "Fizz" if isMultipleOf3(x) else ""


def getBuzzIfMultipleOf5(x):
    return "Buzz" if isMultipleOf5(x) else ""


Main()
