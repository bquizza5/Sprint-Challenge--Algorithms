#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(c) the loop only ever runs 2 times

b)
O(n) the loop will run n (input) times

c)
O(n+1) the function will run one more than n
## Exercise II

I am guessing we are suppose to find floor f as fast as we can?

If so, I would drop an egg at the middle floor = len(n)/2. If the egg didn’t break, I would go to the middle of the top half of the floors and try it again. If the egg did break, I would go to the middle of the bottom half of the stairs and try again. I would do this until I had a short list of floors that I knew floor f was in. Then I would loop through this short list until I found floor f.


