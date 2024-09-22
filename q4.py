def distribute_packages(trucks:list[int], to_load:int) -> int:
    curr_max_load = max(trucks)
    un_even_loads = sum([curr_max_load - i for i in trucks])
    if un_even_loads >= to_load:
        return curr_max_load

    remain_load = to_load - un_even_loads
    each_truck_adder = remain_load // (len(trucks))
    if remain_load % len(trucks):
        each_truck_adder +=1

    return each_truck_adder + curr_max_load



print(distribute_packages([2,3,4,5,6], 11))