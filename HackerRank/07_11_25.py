if __name__ == '__main__':
    N = int(input())
    li: list = []
    for i in range(N):
        func, *line = input().split()
        numbers = list(map(int, line))
        if func == 'print':
            print(li)
        elif func == 'insert':
            li.insert(numbers[0], numbers[1])
        elif func == 'append':
            li.append(numbers[0])
        elif func == 'remove':
            li.remove(numbers[0])
        elif func == 'sort':
            li.sort()
        elif func == 'pop':
            li.pop()
        elif func == 'reverse':
            li.reverse()