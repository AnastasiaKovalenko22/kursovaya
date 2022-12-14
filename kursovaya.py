def algorithm(x, y):
    global my_sum
    if x == -1 and y == -1:
        max = -1
        res_i = -1
        res_j = -1
        for i in range(N):
            if i < n-1 or i > n+1:
                continue
            for j in range(N):
                if j < n-1 or j > n+1:
                    continue
                if map_matrix[i][j] > max:
                    res_i = i
                    res_j = j
                    max = map_matrix[i][j]
                elif map_matrix[i][j] == max and (i < res_i or abs(i - (N-1)) < abs(res_i - (N-1)) or abs(j - (N-1)) < abs(res_j - (N-1)) or j < res_j):
                    res_i = i
                    res_j = j
                    max = map_matrix[i][j]
        my_sum += max
        map_matrix[res_i][res_j] = -1
        return res_i, res_j
    else:
        max = -1
        res_i = -1
        res_j = -1
        for dx in range(-1,2):
            for dy in range(-1,2):
                if abs(dx + dy) != 1:
                    continue
                if map_matrix[x + dx][y + dy] > max:
                    res_i = x + dx
                    res_j = y + dy
                    max = map_matrix[x + dx][y + dy]
        if my_sum + max >= opponent_sum:
            my_sum += max
            map_matrix[res_i][res_j] = -1
            return res_i, res_j
        previous_max = max
        previous_res_i = res_i
        previous_res_j =res_j
        max = -1
        res_i = -1
        res_j = -1
        for dx in range(-1,2):
            for dy in range(-1,2):
                if abs(dx + dy) != 1:
                    continue
                if map_matrix[x + dx][y + dy] > max and x + dx >= 2 and abs((x + dx) - (N - 1)) >= 2 and y + dy >= 2 and abs((y + dy) - (N - 1)) >= 2:
                    res_i = x + dx
                    res_j = y + dy
                    max = map_matrix[x + dx][y + dy]
        if max == -1:
           my_sum += previous_max
           map_matrix[previous_res_i][previous_res_j] = -1
           return previous_res_i, previous_res_j
        my_sum += max
        map_matrix[res_i][res_j] = -1
        return res_i, res_j


map_matrix = []
N = int(input())
n = (N - 1) // 2
for i in range(N):
    map_matrix.append([])
    nums = list(map(int, input().split(" ")))
    for j in range(N):
        map_matrix[i].append(nums[j])
x, y = map(int, input().split(" "))
my_sum = 0
opponent_sum = 0
if x != -1:
    opponent_sum = map_matrix[x][y]
    map_matrix[x][y] = -1

while True:
    my_x, my_y = algorithm(x, y)
    print(str(my_x) + " " + str(my_y))
    x, y = map(int, input().split())
    opponent_sum += map_matrix[x][y]
