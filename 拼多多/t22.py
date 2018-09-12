# 3 4
# .oxo
# o..o
# .xox

def show(table, a, b):
    tag = []
    for k in range(b):
        if table[-1][k] == 'o':
            table[-1] = table[-1][:k] + '.' + table[-1][k + 1:]
        if table[-1][k] == '.':
            tag.append(0)
        else:
            tag.append(1)
    for i in range(1, a):
        for j in range(b):
            if table[a - i - 1][j] == 'x':
                tag[j] = i
            elif table[a - i][j] == '.':
                if tag[j] == 0:
                    table[a - i - 1] = table[a - i - 1][:j] + '.' + table[a - i - 1][j + 1:]
                elif table[a - i - 1][j] == 'o':
                    table[a - i - 1] = table[a - i - 1][:j] + '.' + table[a - i - 1][j + 1:]
                    table[a - tag[j] - 1] = table[a - tag[j] - 1][:j] + 'o' + table[a - tag[j] - 1][j + 1:]
                    tag[j] += 1
                elif table[a - i - 1][j] == 'x':
                    tag[j] = i


if __name__ == '__main__':
    a, _, b = input()
    table = []
    a, b = int(a), int(b)
    for i in range(a):
        table.append(input())
    show(table, a, b)
    for i in range(a):
        print(table[i])
