
def find(group, i, j, matrix):
    if i==10 and j==10:
        print('group nums: ',len(group))
        print('max:',max)


if __name__ == '__main__':
    matrix = []
    with open('input', 'r', encoding='utf8')as fi:
        M, N = fi.readline().strip().split(',')
        M = int(M)
        N = int(N)
        for line in fi.readlines():
            nums = line.strip().split(',')
            matrix.append([int(num) for num in nums])
    count = 0
    max = 0
    all = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==1:
                all.append([i,j])
    for i,j in all:
        while find():
            pass

