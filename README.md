THE PROBLEM
-----------
Odd number of divisors problem:  
>Given 3 inputs A, B and K:  
>where 1 < A < B   
>and K is a positive odd number   
>return the number of integers between A and B inclusive that have exactly K divisors.

A well thought-out and optimised solution will be able to run through large ranges of numbers (range of 10 billion) in a few seconds.


My solution is in the file **evaluate_divisors.js**. It handles large ranges of numbers, completing every test in about 2 seconds, even for ranges of 10 billion . 



To run Jasmine tests to evaluate my solution:  

1. Install node on your machine if you have not already from: https://nodejs.org/en/
2. Install gulp globally using npm
    $ npm install --global gulp-cli
2. Run npm install from the directory containing this file (Ignore any warning messages. However, if you receive any critical errors we suggest that you upgrade your version of Node.js)
    $ npm install
3. Run the server
    $ gulp
4. Open http://localhost:5000/ in a browser

