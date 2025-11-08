def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Questin 1
def count_substring(string, sub_string):
    count: int = 0
    for i in range(0, len(string)-(len(sub_string)-1)):
        new_str: str = ''
        for j in range(len(sub_string)):
            new_str = new_str + string[i+j]
        if (new_str) == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

# Question 2
if __name__ == '__main__':
    s = input()
    result: bool = False
    for i in s:
        if i.isalnum():
            result = True
    print(result)

    result: bool = False
    for i in s:
        if i.isalpha():
            result = True
    print(result)

    result: bool = False
    for i in s:
        if i.isdigit():
            result = True
    print(result)

    result: bool = False
    for i in s:
        if i.islower():
            result = True
    print(result)

    result: bool = False
    for i in s:
        if i.isupper():
            result = True
    print(result)

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))