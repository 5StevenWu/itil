from concurrent.futures import ThreadPoolExecutor
import time

pool = ThreadPoolExecutor(20)


def task(hostname):
    print(hostname)
    time.sleep(1)


for i in range(1, 101):
    hostname = "c{}.com".format(i)

    pool.submit(task, hostname)
