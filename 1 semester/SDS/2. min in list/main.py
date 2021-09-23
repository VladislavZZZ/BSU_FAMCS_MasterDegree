import collections


def insert_right(d: collections.deque, r_stack: list, value: int):
    d.append(value)
    if len(r_stack) == 0:
        r_stack.append((value, value))
    else:
        r_stack.append((value, min(value, r_stack[-1][1])))
    if len(l_stack) == 0:
        return r_stack[-1][1]
    else:
        return min(r_stack[-1][1], l_stack[-1][1])


def insert_left(d: collections.deque, l_stack: list, value: int):
    d.appendleft(value)
    if len(l_stack) == 0:
        l_stack.append((value, value))
    else:
        l_stack.append((value, min(value, l_stack[-1][1])))
    if len(r_stack) == 0:
        return l_stack[-1][1]
    else:
        return min(r_stack[-1][1], l_stack[-1][1])


def remove_right(d: collections.deque, r_stack: list):
    d.pop()
    if len(r_stack) == 0:
        move_data(export_stack=r_stack, import_stack=l_stack)
        r_stack.pop()
        if len(r_stack) == 0:
            return -1
        return r_stack[-1][1]
    else:
        r_stack.pop()
        if len(r_stack) == 0:
            if len(l_stack) == 0:
                return -1
            return l_stack[-1][1]

    return min(l_stack[-1][1], r_stack[-1][1])


def remove_left(d: collections.deque, l_stack: list):
    d.popleft()
    if len(l_stack) == 0:
        move_data(export_stack=l_stack, import_stack=r_stack)
        l_stack.pop()
        if len(l_stack) == 0:
            return -1
        return l_stack[-1][1]
    else:
        l_stack.pop()
        if len(l_stack) == 0:
            if len(r_stack) == 0:
                return -1
            return r_stack[-1][1]
    return min(r_stack[-1][1], l_stack[-1][1])


def move_data(export_stack: list, import_stack: list):
    for i in range(len(import_stack)):
        data = import_stack.pop()
        if len(export_stack) == 0:
            export_stack.append((data[0], data[0]))
        else:
            export_stack.append((data[0], min(export_stack[-1][1], data[0])))


if __name__ == '__main__':
    big_deque = collections.deque()
    r_stack, l_stack = [], []
    # with open('input.txt', 'r') as inpt:
    #     q = int(inpt.readline())
    #     for i in range(q):
    #         req = inpt.readline().split(' ')
    #         if req[0][0] == '-':
    #             if req[0][1] == 'R':
    #                 print(remove_right(deq, r_stack))
    #             else:
    #                 print(remove_left(deq, l_stack))
    #         else:
    #             if req[0][1] == 'R':
    #                 print(insert_right(deq, r_stack, int(req[1])))
    #             else:
    #                 print(insert_left(deq, l_stack, int(req[1])))
    q = int(input())
    for i in range(q):
        req = input().split(' ')
        if req[0][0] == '-':
            if req[0][1] == 'R':
                print(remove_right(big_deque, r_stack))
            else:
                print(remove_left(big_deque, l_stack))
        else:
            if req[0][1] == 'R':
                print(insert_right(big_deque, r_stack, int(req[1])))
            else:
                print(insert_left(big_deque, l_stack, int(req[1])))
