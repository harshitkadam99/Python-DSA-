# recursion is of two types:
# head and tail/(backtracking)
# Recursion tree:
# Head Recursion:-
# function call ho raha haii print ho raha haii fir function call ho raha haii ese chalte chalte jab tak condition satisfy nahi ho rahi jab tak.
# time complexity: O(n)
# Tail Recursion:-
# function call ho raha fir next funxtion call ho raha haii ese hi jab tak condition satisfy nahi ho rahi tab tak uske bad fir print hona suru ho raha hai.
# time complexity: O(n)

# Recursion using parameters:-
def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)
func(15,4)

# print 1 to n using recursion 
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
func(1,5)

def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)
func(1,5)


def func(n):
    if n==0:
        return
    print(n)
    func(n-1)
func(5)

def func(n):
    if n>5:
        return
    print(n)
    func(n+1)
func(1)

print("**********")

# parameterized and functional recursion 
# sum of 1 to n 
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)
func(0,1,5)

def func(n):
    if n==1:
        return 1
    return n+func(n-1)
print(func(5))

# Factorial of the number
def func(n):
    if n==1:
        return 1
    return n*func(n-1)
print(func(5))

# Reverse an array using recusion 
nums = [2,4,3,5,6,9,8,7,1]
def func(nums,l,r):
    if l>=r:
        return
    nums[l],nums[r] = nums[r],nums[l]
    func(nums, l+1, r-1)

def reverseArray(nums,l,r):
    func(nums,l,r)
    return nums

print(reverseArray(nums, 0, len(nums) - 1))

# check if the string is palindrome
s = 'nitin'
def func(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return func(s,l+1,r-1)
print(func(s,0,len(s)-1))

# find the fibonacci number
def func(n):
    if n<=1:
        return n
    return func(n-1)+func(n-2)
print(func(6))