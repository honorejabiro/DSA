# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Brute Force, here we will visit each subproblem and solve it without using memory for solutions for previous calculations

# If we reach a number less than 1 or equal to 1 return n-1
# Recurse the function to find fibonacci of n-2
# Recurse the function to find the fibonacci of n
# Return the sum of fibonacci of n-1 and n

# Time complexity is O(2^n) and the Space complexity is O(1)

def fib(n):

    if n <= 1:
        return n
    
    left = fib(n-1)
    right = fib(n-2)
    return (left + right)

def main():
    n = 5
    print(fib(n))

if __name__ == "__main__":
    main()