import threading
import time


def print_rev_num(num):
    for i in range(num, 0, -1):
        print(f'Current thread: {threading.currentThread().getName()}\n'
              f'Count = {i}')
        time.sleep(1)


if __name__ == '__main__':
    count_from = 10

    t1 = threading.Thread(target=print_rev_num, args=(count_from,))
    t2 = threading.Thread(target=print_rev_num, args=(count_from,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
