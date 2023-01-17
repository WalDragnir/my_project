def row_weights(row: list) -> list:
    rl = [0, 0]
    i = 1
    for num in row:
        if i == 1:
            rl[0] += num
            i += 1
        if i == 2:
            rl[1] += num
            i -= 1
    return rl


row_weights([8, 5, 9, 3])
print(row_weights([2, 3, 5, 6, 99]))

print('fff')
