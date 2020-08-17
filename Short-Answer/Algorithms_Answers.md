#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a increase by n * n for each iteration. since there are n (n * n)'s (by division) it will always take n iterations to complete.


b) It will always take at least n time because of the outer for loop. The inner while loop is a little more tricky. Luckily j starts at one and doubles each iteration, which means it will take j log(n) times to be equal to n. Thus the overall run time is nlog(n)


c) The function will run recusively n + 1 times (+1 because there's one extra iteration for the 0th bunny.)

## Exercise II
I would simply use a binary search. I would keep track of a last, mid, and first floor as in a binary search. Starting at the middle floor, I would drop my first egg. (last = n, first = 1, mid = first + last // 2). If it breaks I would move down half way between my current position and the bottom floor. (set last = mid - 1, first = first, mid = first + last // 2)If it didn't break I would move up half way. (set last = last, first = mid + 1, mid = first + last // 2). I would continue this until until I found the floor. Since the number of possible floors halves each time, it takes at most O(log N) to find f.


(In real life I would start at the bottom floor and move up one floor at a time, because it's most likely going to break by the 2nd floor. O(n) worst case.)


