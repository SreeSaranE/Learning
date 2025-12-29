
# lamda
fun1 = lambda f, q: f + q
text: str = fun1('hello ', 'world')
print(text)

# list comprehension
list1: list = [1,2,3,4,5]
up_list: list = [num ** 2 for num in list1]
print(up_list)

# max of three numbers
a: int = 12
b: int = 9
c: int = 21

if a > b and a > c:
    print(a)

if b > a and b > c:
    print(b)

if c > b and c > a:
    print(c)

print(max(a, b, c))


# count vowels
vow: list = 'a e i o u'.split(' ')
text: str = "Hello World"

count: int = 0
for i in text:
    if i in vow:
        count += 1

print(count)


# count factorial
def fac(n):
    if n == 0:
        return 1
    else:
        return n * (fac(n-1))

print(fac(5))


# convert string to integer
text: str = '20'
num: int = int(text)
print(type(num))


# prime number
def prime(n):
    half = n // 2
    if n < 2:
        return("neither prime nor composite!")

    for i in range(2, int(n * 0.5)+1):
        if n % i == 0:
            return("not a prime")

    return("prime")

for i in range (11):
    print(prime(i))


# palindrome
text: str = '12321'
print(text == text[::-1])


# armstrong number
num: int = 153
digits = [int(d) for d in str(num)]
total = sum(d**(len(digits)) for d in digits)
print("Armstrong" if num == total else "not a armstrong")


# Leap year
year: int = 2025
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")


# Fibanocci sepuence
num: int = 5
ini_list: list = []
while len(ini_list) <= num-1:
    if len(ini_list) < 2:
        ini_list.append(len(ini_list))
    else:
        ini_list.append(sum(ini_list[-2:]))

print(ini_list)