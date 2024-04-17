# CMPS 2200 Assignment 3
## Answers

**Name:** Sofia Della Rosa


Place all written answers from `assignment-03.md` here for easier grading.

1. a) Find the largest *2^k* such that *2^k* <= N. --> then subtract *2^k* from N which is N - *2^k*. --> repeat this until N <= 1.
   
   b) "Prove that this algorithm is optimal by proving the greedy choice and optimal substructure properties."
   
   This algorithm is optimal because --> k is a maximum every time. The largest value a coin can have is always less than or equal to the value of N.

   c) Work = O(log(n)) 
      Span = O(n)
2. a) "give a counterexample that shows that the greedy algorithm does not produce the fewest number of coins."
   counterexample: D = 1, 5, 8 and N = 15 --> algorithm returns 4 coins (8, 5, 1, 1) --> the optimal solution is 3 coins worth 5 each.
   
   b) To find the optimal substructure, all of the different combinations of coins to make N value would need to be calculated. The optimal substructure would be the least amount of coins to make N value.

   c) top-down --> account for each substructure without repetitions using recursion.
    Work = O(n); Span = O(n)

3. for fast_MED and fast_align_MED, not sure why last test for each returns None in testing file. I messed with values, and would appreciate an explanation after grading. 
