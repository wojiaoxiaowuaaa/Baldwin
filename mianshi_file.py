from suanfa.is_prime import is_prime
from gongju.color_print import color_print_greep


def file_write():
    filenames = ('/Users/wl/Desktop/a.txt', '/Users/wl/Desktop/b.txt', '/Users/wl/Desktop/c.txt')
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

    color_print_greep()


if __name__ == '__main__':
    file_write()
