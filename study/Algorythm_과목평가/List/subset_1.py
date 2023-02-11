set = [-7, -3, -2, 5]
subset = [0, 0, 0, 0]

for i in range(2):
    subset[0] = i
    for j in range(2):
        subset[1] = j
        for k in range(2):
            subset[2] = k
            for p in range(2):
                subset[3] = p
                print(set*subset)
