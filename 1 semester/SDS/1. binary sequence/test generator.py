

if __name__ == '__main__':
    n = 20
    k = 2**n - 1
    with open('input.txt', 'w') as out:
        out.write(str(n)+'\n')
        out.write('0')
        for i in range(n-1):
            out.write(' 0')
        out.write('\n'+str(k))