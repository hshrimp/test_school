def find(tag, n):
    global length, point
    if point >= lengn:
        return 0
    if length > len(n) / 2:
        point += 1
        n = n[1:]
        find(n[0], n)

    for char in n:
        if tag != char:
            length += 1
            find(n[:length], n)


if __name__ == '__main__':
    a, _, b = input()
    num = str(int(a) / int(b)).split('.')[1]
    point = 0
    length = 1
    lengn = len(num)
    find(num[0], num)
    print(point, length)
