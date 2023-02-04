def all_list_sum(num_list):
    total = 0
    for list in num_list:
        for num in list:
            total += num
    return total

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))