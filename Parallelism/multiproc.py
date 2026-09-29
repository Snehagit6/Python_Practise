import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

#Multiprocessing
def compute_square(iter):
    
    x = [iter**2 for _ in range(50000)]  # Simulates a CPU-bound task
    print(f"Finished computing square : {x}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    # Normal execution: 
    # compute_square(iter=5)
    # compute_square(iter=10)

    # Using Process
    process1 = Process(target=compute_square, args=(5,))
    process2 = Process(target=compute_square, args=(10,))
    process1.start()
    process2.start()
    
    # Wait for both processes to finish before moving the main script forward
    process1.join()
    process2.join()
    print(f"total time taken: {time.perf_counter() - start_time:.2f} seconds")