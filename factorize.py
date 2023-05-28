import time
import logging
import concurrent.futures
from multiprocessing import Pool, cpu_count


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def factorize(number):
    result = []
    for i in range(1, number+1):
        if number % i == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    start_1 = time.time()
    a, b, c, d = factorize(128), factorize(255), factorize(99999), factorize(10651060)
    end_1 = time.time()
    logging.info(f'Time taken synchronously: {end_1 - start_1}')

    start = time.time()
    with Pool(cpu_count()) as p:
        results = p.map(factorize, [128, 255, 99999, 10651060])
        p.close()
        p.join()
    end = time.time()
    logging.info(f'Time taken with Pool: {end - start}')

    start_3 = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results_new = executor.map(factorize, [128, 255, 99999, 10651060])
    end_3 = time.time()
    logging.info(f'Time taken with ProcessPoolExecutor: {end_3 - start_3}')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

