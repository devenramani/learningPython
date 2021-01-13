"""""
A recursive function is a function that calls itself. When writing such functions, it is important that
you build in a stopping condition that controlswhen the recursive calls stop. Otherwise, the function
would keep calling itself indeterminately. 

a) Write a recursive function that computes the factorial of a parameter n. Use the following
formula:
𝑛! = 𝑛(𝑛 − 1)!

b) In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient method for
computing the greatest common divisor (GCD) of two numbers a and b, i.e. the largest
number that divides both of them without leaving a remainder. Write a recursive function
gcd that computes the greatest common divisor of two number by using Euclid’s algorithm.

𝑔𝑐𝑑(𝑎,𝑏) = 
{
𝑔𝑐𝑑(𝑏,𝑎 − 𝑏) 𝑖𝑓 𝑎 > 𝑏
𝑎 𝑖𝑓 𝑎 = 𝑏
𝑔𝑐𝑑(𝑎,𝑏 − 𝑎) 𝑖𝑓 𝑎 < 𝑏

"""""

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def gcd(a,b):
    if a==b:
        return a 
    elif a>b:
        return gcd(b,a-b)
    else:
        return gcd(a,b-a)

print(gcd(2,4))
