
combinations = {}
for i in range(1, 7):
    for j in range(1, 7):
        sum_of_dice = i + j
        if sum_of_dice not in combinations:
            combinations[sum_of_dice]=1

        else:
            combinations[sum_of_dice]+=1
print(combinations)
