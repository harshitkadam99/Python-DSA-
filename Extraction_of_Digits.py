n = 5873
num = n
while num > 0:
    digit  = num % 10
    print(digit)
    num = num//10

#### count of digits 
n = 5873
num = n
count  = 0
while num > 0:
    count += 1
    num = num//10
print(count)


#####
def count_digits(n):
    num = n
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

print(count_digits(5378))

#####
from math import log10

def count_digits(num):
    num = abs(num)
    if num == 0:
        return 1
    return int(log10(num) + 1)

print(count_digits(5873))


#### check palindrome number
n = 1234
num = n
result = 0
while num > 0 :
    last_digit = num % 10
    result  =result * 10 + last_digit
    num = num // 10
if result == n:
    print("it is a palindrome")
else:
    print("not a palindrome")

n = 1221
num = n
result = 0
while num > 0 :
    last_digit = num % 10
    result  = result * 10 + last_digit
    num = num // 10
if result == n:
    print("it is a palindrome")
else:
    print("not a palindrome")

n = "nitin"
rev = ""

for ch in n:
    rev = ch + rev

if rev == n:
    print("it is a palindrome")
else:
    print("not a palindrome")


#### Armstrong Number
n = 153
num = n
order = 3
result = 0
while num > 0:
    digit = num % 10
    ## result += digit ** order
    result = result + (digit ** order)
    num = num // 10
if result == n:
    print ("it is an armstrong number")
else:
    print("not an armstrong number")


##### print factor/divisors
n = 20
num = n
result = []
for i in range (1, num+1):       #(brute force solution)#
    if num % i == 0:
        result.append(i)
print(result)

n = 20
num = n
result = []
for i in range (1, num//2+1):       #(brute force solution)#
    if num % i == 0:
        result.append(i)
#print(result)
result.append(n)
print(result)

n = 36
num = n
from math import isqrt
result = []
for i in range (1, isqrt(num)+1):     #(optimal solution)#
    if num % i == 0:
        result.append(i)
        if i !=num // i:
            result.append(num // i)
# result.sort()
print(result)