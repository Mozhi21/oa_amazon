from collections import Counter

def get_max_info(data_set: list[str], max_common_feature: int) -> int:
    holder = dict()
    n = len(data_set)
    for s in data_set:
        curr_counter = Counter(s)
        curr_holder =[0] * 26
        for i, count_i in curr_counter.items():
            curr_holder[ord(i) - ord("a")] = count_i
        holder[s] = curr_holder

    print(holder)

    res = 0

    for i in range(n):
        for j in range(i):
            a, b = holder[data_set[i]],holder[data_set[j]]
            shared_count = sum([min(a[k] , b[k]) for k in range(26)])
            print("diff", shared_count)
            if shared_count > max_common_feature:
                continue
            res = max(res, abs(len(data_set[i]) - len(data_set[j])))

    return res

print(get_max_info(["abofh", "ab", "mo"], 1))            
print(get_max_info(["a", "bcdef"], 1))            
    