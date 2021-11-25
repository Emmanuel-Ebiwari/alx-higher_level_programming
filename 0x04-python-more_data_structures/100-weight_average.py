#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    mul = 0
    sum_up = 0
    ave = 0
    for i in range(len(my_list)):
        mul += my_list[i][0] * my_list[i][1]
        sum_up += my_list[i][1]
    ave = mul / sum_up
    return ave
