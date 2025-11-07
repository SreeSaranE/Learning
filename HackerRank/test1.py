if __name__ == '__main__':
    n: int = ['1', '2', '3', '4']
    p = (list(map(int , n)))
    print(list(map(lambda q: q*2 , p)))