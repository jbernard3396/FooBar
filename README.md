# FizzBuzz
## Goal
Solve the classic FizzBuzz problem without ever using more than two [logical lines of code](#logical-lines-of-code) in a single function


## Purpose
The purpose of this exercise is to test the limits of abstraction and single responsibility functions.  I plan to write my functions so that they document themselves while using as little commenting as possible

## Problem Description

### FizzBuzz
FizzBuzz is a well known programming problem whereby you must print the numbers from 1 to 100 and you must print 'Fizz' instead of each number that is a multiple of three and 'Buzz' instead of each number that is a multiple of five. Numbers that are multiples of three and five mut be replaced by 'FizzBuzz'  
Here is the [Wikipedia article](https://en.wikipedia.org/wiki/Fizz_buzz)

### Logical Lines of Code
Logical lines of code have been historically rather difficult to measure. I have two general rules regarding lines of code
#### 1. Follow normal standards in separating lines

```
def examplePythonFunction0():
  if(True):
    print('hello')
```
Would be two lines of code (the 'if' line and the 'print' line).  I cannot reduce the number of lines by writing
```
def examplePythonFunction1():
  if(True):print('hello')
```
Though this is one physical line of code, it is still two logical lines of code.  

#### 2. Lines that are pure syntax or white space do not count as logical line of code:

   ```
func exampleC++Function0(){
  if(true){
    cout<<'hello';
   }
}
```
and
```
func exampleC++Function1(){
  if(true){
    cout<<'hello'; }
}
```
Would both be two logical lines of code because the closing bracket is pure syntax.

## Future Work
Should this first exercise be successful, I may change the name of this project to be more generic and add more exercises with these same rules
