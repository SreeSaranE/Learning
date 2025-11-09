# Question 3
def swap_case(s):
    str_list: list = list(s)
    for i in range(len(str_list)):
            if str_list[i].islower():
                 str_list[i] = str_list[i].upper()
            else:
                 str_list[i] = str_list[i].lower()
    return "".join(str_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Question 4
def split_and_join(line):
    list_str: list = line.split(" ")
    new_list: list = "-".join(list_str)
    return new_list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Question 5
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# https://drive.google.com/file/d/1BUa4DBoNg8jAuIauxx22r_Ci2uWr_rI1/view?usp=drive_link
text = ".|."
input1 = input()
num = input1.split(" ")
loop = int(num[0])
width = loop*3
stop = loop//2
count = 1
for i in range(1, loop):
    repeat = text*count
    count = count+2
    print(repeat.center(width,'-'))
    if i == stop:
        print("WELCOME".center(width,'-'))
        for i in range(count-2 , 0, -2):
            repeat = text*i
            print(repeat.center(width,'-'))
        break