THE PROBLEM
-----------
Odd number of divisors problem:  
>Given 3 inputs A, B and K:  
>where 1 < A < B   
>and K is a positive odd number   
>return the number of integers between A and B inclusive that have exactly K divisors.

A well thought-out and optimised solution will be able to run through large ranges of numbers (range of 10 billion) in a few seconds.

Solution and explanation:
---
My solution is in the file **evaluate_divisors.js**. It handles large ranges of numbers, completing every test in about 2 seconds, even for ranges of 10 billion . 

>Returns number of ints from a to b inclusive that have exactly k divisors, where k is odd.  
>The guarentee that k is odd allows us to make some optimizations and not have to iterate over the entire range from a to b (which would take way too long). The only case a number has an odd number of divisors is if it's a perfect square, so two of it's roots are the same number. 

>This means we can just iterate over perfect squares from a to b. We do this by finding the smallest and largest square root in the range and iterating over the roots themselves, meaning we only ever look at perfect squares in range(a, b+1).  
>checking if a prefect square n has a certain number of divisors is then a simple task, dividing n by ints in range(1, sqrt(n)) and checking the remainder. 

>Further small optimisations can be made when checking if a perfect square n has k divisors, such as not checking any even factors if the square is odd. 


I have written soltutions in both Python and Javascript.  

The Python scripts can be set to executable and run from a terminal:  
>1 $ chmod 744 odd-divisors_optimized.py  
>2 $ ./odd-divisors_optimized.py

Interestingly enough, the Python implementation runs much slower than the Javascript does, even though the algorithm is the same. To illustrate that the solution is still the correct, optimized version, there is a brute-force Python solution that the optimized solution can be compared against. You will find that the optimized version runs *much* faster than the other. 

To run Jasmine tests to evaluate my Javascript solution:  

>1. Install node on your machine if you have not already from: https://nodejs.org/en/
>2. Install gulp globally using npm
>    $ npm install --global gulp-cli
>2. Run npm install from the directory containing this file (Ignore any warning messages. However, if you receive any critical errors i suggest that you upgrade your version of Node.js)
>    $ npm install
>3. Run the server
>    $ gulp
>4. Open http://localhost:5000/ in a browser

