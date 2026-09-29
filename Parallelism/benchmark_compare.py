import time
from multiprocessing import Process, Queue
from concurrent.futures import ProcessPoolExecutor


def square_generator(n, limit=5000000):
    for i in range(limit):
        yield (n + i) ** 2


def compute_square(n, limit=5000000):
    return sum(square_generator(n, limit))


def worker(n, queue):
    queue.put((n, compute_square(n)))


def normal_execution():
    start = time.perf_counter()
    result1 = compute_square(5)
    result2 = compute_square(10)
    end = time.perf_counter()
    print(f"Normal execution result: {result1}, {result2}")
    print(f"Normal execution time: {end - start:.4f} sec")


def multiprocessing_execution():
    start = time.perf_counter()
    queue = Queue()

    p1 = Process(target=worker, args=(5, queue))
    p2 = Process(target=worker, args=(10, queue))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    result1 = queue.get()
    result2 = queue.get()
    end = time.perf_counter()
    print(f"Multiprocessing result: {result1}, {result2}")
    print(f"Multiprocessing time: {end - start:.4f} sec")


def process_pool_execution():
    start = time.perf_counter()

    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(compute_square, 5), executor.submit(compute_square, 10)]
        results = [f.result() for f in futures]

    end = time.perf_counter()
    print(f"ProcessPoolExecutor result: {results}")
    print(f"ProcessPoolExecutor time: {end - start:.4f} sec")


if __name__ == "__main__":
    normal_execution()
    multiprocessing_execution()
    process_pool_execution()
