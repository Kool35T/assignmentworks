#i) log(n)

#ii) The log(n) (Logarithmic) function grows very slowly. N^2 (Exponential functions) are the inverse of log(n) (Logarithmic) function, which grows very rapidly

#iii)
#1. Let min = 0 and max = n-1.
#2. If ___min___ is greater than ___max___, then stop: target is not present in array. Return -1
#3. Compute guess as the ____middle____ of max and min, rounded down (so that it is an integer)
#4. If array[guess] equals target, then stop. You found it! Return guess
#5. If the guess was too low, that is, array[guess] < target, then set min = ____guess+1____
#6. Otherwise, the guess was too high. Set max = ____guess-1____
#7. Go back to step
