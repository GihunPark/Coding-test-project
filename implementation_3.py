index = input()
row = int(index[1])
col = int(ord(index[0]))  - int(ord('a')) + 1
count = 0
x = row
y = col
a = [2, 2, -2, -2, 1, 1, -1, -1]
b = [1 , -1, 1, -1, 2, -2, 2, -2]
for i in range(8):
    xNew = x + a[i]
    yNew = y + b[i]
    if xNew >= 1 and yNew >= 1 and xNew < 9 and yNew <9:
        count += 1
print(count)