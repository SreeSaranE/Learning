import textwrap

#long_text = "abcdefghijklmnopqrstuvwxyz"
long_text = 'abc'
com_list = []
new_list = []

for i in range(1, len(long_text)):
    loop_1: str = long_text
    while len(loop_1) != 0:
        wrapped_lines = textwrap.wrap(long_text, i)
        #print(i, wrapped_lines)
        new_list.append(wrapped_lines.pop(-1))
        com_list.extend(wrapped_lines)
        loop_1 = loop_1[1:]
    print("New: ", new_list)
    print("Complete: ", set(com_list))

new_list = list(set(new_list))
print("-"*40)
com_list.extend(new_list)
print(com_list)