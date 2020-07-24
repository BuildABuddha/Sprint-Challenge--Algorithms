#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This function has O(N) complexity because the while loop will loop through however many times N is. 

b)
This function appears to have O(N*log(N)) complexity because the first loop is O(N) and the inner loop is less complex than the first. 

c)
This recursive function has O(N) complexity, since it will call itself one additional time as N goes up by one. 

## Exercise II
We have a building of n floors, and at floor f and above, an egg dropped with break, and at floor f-1 and lower, an egg will not break. 

We can simulate this building with an array of length n+1 filled with booleans, with building[:f] set to False and building[f:] set to True. This will be the input of the function. We need to find the index f and return it in as few egg drops as possible.

The code will look something like this:

```
set n to length of building array
set low to 1
set high to n
set mid to integer (low + high) / 2

while high > low:
    if building[mid] is True and building[mid - 1] is False:
        return mid
    
    else if building[mid] is True:
        set high to mid - 1
        set mid to integer (low + high) / 2

    else if building[mid] is False:
        set low to mid + 1
        set mid to integer (low + high) / 2

return -1
```

This should only require O(log(n)) time complexity, and should greatly reduce the number of drops required from the basic approach of dropping an egg at every floor as you go up. 
