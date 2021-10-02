import collections


def get_min(r_stack: list, l_stack: list):
    r_len = len(r_stack)
    l_len = len(l_stack)
    if r_len == 0 or l_len == 0:
        if r_len == 0 and l_len == 0:
            return -1
        elif r_len == 0:
            return l_stack[-1][1]
        else:
            return r_stack[-1][1]
    else:
        return min(r_stack[-1][1], l_stack[-1][1])


def insert_right( r_stack: list, value: int):
    if len(r_stack) == 0:
        r_stack.append((value, value))
    else:
        r_stack.append((value, min(value, r_stack[-1][1])))
    return get_min(r_stack,l_stack)



def insert_left(l_stack: list, value: int):
    if len(l_stack) == 0:
        l_stack.append((value, value))
    else:
        l_stack.append((value, min(value, l_stack[-1][1])))
    return get_min(r_stack,l_stack)


def remove_right(r_stack: list):
    if len(r_stack) == 0:
        move_data(export_stack=r_stack, import_stack=l_stack)
    r_stack.pop()
    return get_min(r_stack,l_stack)


def remove_left(l_stack: list):
    if len(l_stack) == 0:
        move_data(export_stack=l_stack, import_stack=r_stack)
    l_stack.pop()
    return get_min(r_stack,l_stack)


def move_data(export_stack: list, import_stack: list):
    for i in range(len(import_stack)):
        data = import_stack.pop()
        if len(export_stack) == 0:
            export_stack.append((data[0], data[0]))
        else:
            export_stack.append((data[0], min(export_stack[-1][1], data[0])))


if __name__ == '__main__':
    r_stack, l_stack = [], []
    # q = int(input())
    # for i in range(q):
    #     req = input().split(' ')
    #     if req[0][0] == '-':
    #         if req[0][1] == 'R':
    #             print(remove_right(deq, r_stack))
    #         else:
    #             print(remove_left(deq, l_stack))
    #     else:
    #         if req[0][1] == 'R':
    #             print(insert_right(deq, r_stack, int(req[1])))
    #         else:
    #             print(insert_left(deq, l_stack, int(req[1])))
    with open('input.txt', 'r') as inpt:
        q = int(inpt.readline())
        for i in range(q):
            req = inpt.readline().split(' ')
            if req[0][0] == '-':
                if req[0][1] == 'R':
                    print(remove_right(r_stack))
                else:
                    print(remove_left(l_stack))
            else:
                if req[0][1] == 'R':
                    print(insert_right(r_stack, int(req[1])))
                else:
                    print(insert_left(l_stack, int(req[1])))
