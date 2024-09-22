"""
    在一串 地点中间 建两个数据中心，要求 每个地点必须连接到某一个数据中心，并且用的网线最短

    先做前序和， 后续和， 这样 给定一个区间可以快速求
"""

def build_warehouses(dist_centers:list[int]) -> int:
    prefix =[]
    postfix =[]
    n = len(dist_centers)
    curr_sum = 0
    for i in range(n):
        curr_sum += dist_centers[i]- dist_centers[0]
        prefix.append(curr_sum)
    curr_sum = 0
    for i in range(n-1, -1, -1):
        
        curr_sum += dist_centers[n-1] - dist_centers[i]
        postfix.append(curr_sum)
    postfix = postfix[::-1]
    def _calc_distance(start, end):
        center = (start + end) // 2
        left = prefix[center] - prefix[start] - (dist_centers[start]-dist_centers[0]) * (center - start)
        right = postfix[center] - postfix[end] - (dist_centers[-1] - dist_centers[end]) * (end - center)
        print("in-calc",left, right)
        print("in-clac detail right", postfix[center], postfix[end],  (dist_centers[-1] - dist_centers[end]) , (center - end))
        return left + right
    
    print(prefix, postfix)
    res = float("infinity")
    for cut in range(1, n):
        left1, left2 = 0, cut
        right1, right2 = cut-1, n-1
        a = _calc_distance(left1, right1)
        b = _calc_distance(left2, right2)
        print(left1, right1, left2, right2)
        print(a,b)
        res = min(res, a + b)
    
    return res

print(build_warehouses([1,2,3]))