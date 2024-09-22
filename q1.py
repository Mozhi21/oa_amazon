from bisect import bisect_left
"""
    车上一堆盒子，可以扔掉一些。要求扔掉最少的盒子，使得 min 盒子 * capacity 》= max 盒子

    sort 以后， 每个盒子都可以是min 盒子， binary search 对应的最大盒子， 计算 对应扔掉几个，
"""

def min_unload(boxes:list[int], capacity:int) -> int:

    def _binary_search(target):
        lo, hi = -1, n
        while lo < hi -1:
            mid = (lo + hi) // 2
            if boxes[mid] <= target:
                lo = mid
            else:
                hi = mid
        return hi
    
    boxes.sort()
    n = len(boxes)
    curr_unloaded = n
    for start in range(n):
        target = boxes[start] * capacity
        end = _binary_search(target)
        curr_unloaded = min(curr_unloaded, start + (n - end))
    
    return curr_unloaded

print(min_unload([1,4,3,2], 2))
print(min_unload([4,5,3,8,3,7], 2))