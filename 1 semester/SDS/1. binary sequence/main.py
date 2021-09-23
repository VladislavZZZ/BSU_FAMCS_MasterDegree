import math

# import numpy as np
import datetime

def fraction_reduction(numerator, denominator):
    k = math.gcd(numerator, denominator)
    return numerator // k, denominator // k

def inc(arr: list):
    i = 0
    while arr[i] == 1:
        arr[i] = 0
        i += 1
    arr[i] = 1
    return i+1

def bseq_to_int(seq: str):
    return int(seq,2)

def get_changes_from_inc(number, bit_len):
    counter = 0
    max_changes = [0 for i in range(bit_len)]
    for i in range(bit_len):
        change_per_inc = number//2**i
        counter += change_per_inc
        max_changes[i] = change_per_inc
    return counter, max_changes


if __name__ == '__main__':
    strt = datetime.datetime.now()
    with open('input.txt', 'r') as inpt:
        k = int(inpt.readline())
        bitseq = inpt.readline().replace(' ','')
        # bits = np.array(inpt.readline().split(' '), np.int)
        increment_num = int(inpt.readline())

    # k = int(input())
    # bitseq = input().replace(' ','')
    # increment_num = int(input())

    number = bseq_to_int(bitseq)
    incremented_num = number + increment_num

    counter1, max_changes1 = get_changes_from_inc(number,k)
    counter2, max_changes2 = get_changes_from_inc(incremented_num,k)
    dif_num = 0
    for i in range(k):
        if max_changes2[i]>max_changes1[i]:
            dif_num+=1

    numerator, denominator = fraction_reduction(counter2-counter1, increment_num)
    print('time spent ', datetime.datetime.now() -strt)
    print(dif_num)
    print(str(numerator)+'/'+str(denominator))