import math

# import numpy as np
import datetime

def fraction_reduction(numerator, denominator):
    k = math.gcd(numerator, denominator)
    return numerator // k, denominator // k


# def inc(arr: np.ndarray):
#     i = arr.size - 1
#     while arr[i] == 1:
#         arr[i] = 0
#         i -= 1
#     arr[i] = 1  # setOne
#     return arr.size - i

def inc(arr: list):
    i = 0
    while arr[i] == 1:
        arr[i] = 0
        i += 1
    arr[i] = 1  # setOne
    return i+1


if __name__ == '__main__':
    start = datetime.datetime.now()
    with open('input.txt', 'r') as inpt:
        k = int(inpt.readline())
        arr = inpt.readline().split(' ')
        arr.reverse()
        # bits = np.array(inpt.readline().split(' '), np.int)
        bits = [int(item) for item in arr]
        increment_num = int(inpt.readline())

    # k = int(input())
    # arr = input().split(' ')
    # arr.reverse()
    # # bits = np.array(inpt.readline().split(' '), np.int)
    # bits = [int(item) for item in arr]
    # increment_num = int(input())

    max_changed_bits = 0
    sum_changed_bits = 0
    for i in range(increment_num):
        num_changes = inc(bits)
        # if i%1000000==0:
        #     print(i)
        if num_changes > max_changed_bits:
            max_changed_bits = num_changes
        sum_changed_bits += num_changes
    av_numerator, av_denominator = fraction_reduction(sum_changed_bits, increment_num)
    print('time -',datetime.datetime.now() - start)
    print('max ch - ',max_changed_bits)
    print('av change', str(av_numerator)+'/'+str(av_denominator))
