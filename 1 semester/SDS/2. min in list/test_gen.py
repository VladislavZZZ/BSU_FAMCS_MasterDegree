if __name__ == '__main__':
    count = 10**6
    with open('input.txt', 'w') as inn:
        inn.write(str(count)+'\n')
        for i in range(count):
            inn.write('+R '+str((i+1)*10)+'\n')