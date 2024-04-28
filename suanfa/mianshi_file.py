from suanfa.is_prime import is_prime


def file_write():
    filenames = ('/Users/wl/Desktop/aaa.txt', '/Users/wl/Desktop/aaab.txt', '/Users/wl/Desktop/aaac.txt')
    l = []
    try:
        for file in filenames:
            l.append(open(file, 'w'))
        for num in range(1, 1000):
            if is_prime(num):
                if num <= 10:
                    l[0].write(str(num) + '\n')
                elif num <= 100:
                    l[1].write(str(num) + '\n')
                else:
                    l[2].write(str(num) + '\n')
    except IOError as e:
        print(e)
    finally:
        for f in l:
            f.close()


if __name__ == '__main__':
    file_write()
