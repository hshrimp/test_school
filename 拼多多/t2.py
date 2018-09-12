import numpy as np

count = 0


def find(hp, na, ba):
    global count
    if hp <= 0:
        return count
    if hp >= ba:
        count += 2
        hp -= ba
        find(hp, na, ba)
    elif hp>2*na:
        count+=2
        return count
    else:
        count += 1
        hp -= na
        find(hp, na, ba)


if __name__ == '__main__':
    hp = int(input())
    na = int(input())
    ba = int(input())
    if ba <= 2 * na:
        if hp / na > hp // na:
            print(hp // na + 1)
        else:
            print(hp // na)
    else:
        find(hp, na, ba)
        print(count)
