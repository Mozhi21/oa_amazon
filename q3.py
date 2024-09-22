def find_outlier(arr : list[int]) -> int:
    total = sum(arr)
    holder = set(arr)
    res = -1 * float("infinity")
    for num in arr:
        curr_total = total - num
        if curr_total % 2:
            continue
        if curr_total // 2 in holder:
            res = max(num, res)
    
    return res

print(find_outlier([4,1,3,16,2,10]))