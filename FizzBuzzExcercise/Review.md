# Mission Review
Mission was successful.  I was able to get the exact functionality I wanted with out any functions which had more than 2 logical lines of code and I did not have to use anything particularly clever either.

# Statistical comparison of limited to regular file

| Category                 | Regular       | Limited | Extra Limited |
| ------------------------ |:-------------:|:-------:|:-------------:|
| Physical Lines           | 22            | 80      | 45            |
| Logical Lines            | 27            | 12      | 20            |
| Functions                | 16            | 2       | 10            |
| ComparisonsPerIteration  | 13            | 2.63    | 4             |
| RecycleFactor*           | .62           | .40     | .83           |
| #ClarifyingComments      | 0             | 1       | 0             |

*Recycle Factor is a measurement metric that I Created to measure how well code is recycled.
In most cases it will vary between 0 and 1 where lower is better. It is measured by simply 
putting the number of functions declared by the number of times declared functions are called.  In larger programs it 
might be useful for understanding how well generalization is employed.  For this purpose it probably tells us little. 
But data is always good, right

# Analysis of FizzBuzzLimited

There is an abundance of highly specific functions in the limited version that can only be distinguished from each 
other by absurdly long names.  Since the functions do very limited things, the names are nearly as long as their 
functionality, and have the only way to make them specific enough to be accurate is to enumerate every line of code 
in the function in the function name.

Organization is also very difficult.  The general convention of listing major functions in order of use followed by 
their helper functions with functions that help multiple major functions at the end makes no sense with these 
constraints.  Instead I chose to list functions from top to bottom depending on how high level they were.

The other interesting thing that I noticed was that the general strategy was to consider all of the cases and break 
them off one at a time.  This is essentially what an if else does, which I suppose makes sense, since I was simply 
implementing an If else  

