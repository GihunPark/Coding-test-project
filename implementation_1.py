N = int(input())
moves = input().split()
row, col = 1, 1
## L R U D
drow = [0, 0, -1, 1]
dcol = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
            newRow = row + drow[i]
            newCol = col + dcol[i]
    if newRow < 1 or newCol <1 or newRow > N or newCol > N:
        continue

    row = newRow
    col = newCol

print(row, col)
