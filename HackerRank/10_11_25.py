'''
# https://drive.google.com/file/d/1T3lEIXZsAMfeGdB_oLDRcr37prMr10ya/view?usp=drive_link
def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range (1,number+1):
        decimal=str(i)
        octal=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        binary=bin(i)[2:]
        print(decimal.rjust(width), octal.rjust(width), hexa.rjust(width),binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# https://drive.google.com/file/d/1sJs16RaqkqFLM66AGhbjTif9BI_mmijY/view?usp=drive_link
import string

def print_rangoli(size):
    alpha = list(string.ascii_lowercase)
    num: int = size

    cal: int = num+(num-1)
    new_cal: int = cal+cal-1
    mem_alp: str = ""

    result: list = []
    main_loop: int = (num*2) - 1
    for i in range(num):
        if i == 0:
            mem_alp = alpha[num-1]
        else:
            mem_alp = mem_alp[:i] + alpha[num-i-1] + mem_alp[i-1:]

        new_str: str = ''
        loop: int = 0
        for letter in mem_alp:
            if loop == len(mem_alp) - 1:
                new_str += letter
                break
            new_str += letter + '-'
            loop += 1

        result.append(new_str.center(new_cal, '-'))

    loop = 2
    for i in range((len(result)*2) - 1):
        if i < len(result):
            print(result[i])
        else:
            print(result[i- loop])
            loop += 2

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
'''
# https://drive.google.com/file/d/14HQIdZrOhE7SlW8gzQceN0Tf2dekp7n0/view?usp=drive_link
def solve(s):
    words: list = s.split(" ")
    new_words: list = []
    for i in words:
        new_words.append(i.capitalize())
    return " ".join(new_words)

print(solve("Hello there"))