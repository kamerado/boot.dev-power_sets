#!/usr/bin/env python3
def assign_bin(input_set):
    dict = {}
    for i in range(0, len(input_set)):
        dict[i + 1] = input_set[i]
    # print(dict)
    return dict


def bin_num_iter(input_set):
    num_bits = len(input_set)
    for i in range(2**num_bits):
        binary = bin(i)[2:].zfill(num_bits)
        yield binary


def bin_array(bin_num):
    return [int(digit) for digit in bin_num]


def power_set(input_set):
    result = []
    tmp = []
    dic = assign_bin(input_set)
    if len(input_set) == 0:
        return [[]]
    for bin_num in bin_num_iter(input_set):
        bin_arr = bin_array(bin_num)
        print(bin_arr)
        bin_arr.reverse()
        for i in range(0, len(input_set)):
            if bin_arr[i]:
                tmp.append(dic[i + 1])
        result.append(tmp)
        tmp = []
    return result
