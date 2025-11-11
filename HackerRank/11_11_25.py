# https://drive.google.com/file/d/19BBy4lx0NaLL4w3XfbyE8r3wflE9tBuu/view?usp=drive_link
import textwrap

def check_repeat(string):
    pass


def minion_game(string):
    # your code goes here
    complete_list: list[str] = list(string)
  #  print(complete_list)
    loop_1: str = string
    inner_loop = 0
    outer_loop = 0
    for i in range(2, (len(string)+1)):
        loop_1: str = string
        while len(loop_1) != 0:
            temp_list: list = textwrap.wrap(loop_1, i)
            print("1st temp",temp_list)
            for j in temp_list:
                if len(j) < len(temp_list[0]):
                    print("Going to remove", j)
                    temp_list.remove(j)
            print("Temp", temp_list)
            complete_list.extend(temp_list)
            loop_1 = loop_1[1:]

            print("Inner Loop: ", inner_loop)
            inner_loop += 1
            
            print("-"*40)

        print("Outer Loop: ", outer_loop)
        outer_loop += 1

    #print((complete_list))

if __name__ == '__main__':
  #  s = input()
    minion_game("hello")