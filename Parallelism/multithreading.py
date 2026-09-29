import threading
import time
from concurrent.futures import ThreadPoolExecutor

#Multithreading
def fetch_data(api_name, delay):
    print(f"Starting fetch from {api_name}...")
    time.sleep(delay)  # Simulates waiting for a network response
    print(f"Finished fetching from {api_name}!")

if __name__ == "__main__":
    start_time = time.perf_counter()
    # Sequential execution: 5 seconds
    # fetch_data("API_1", 3)
    # fetch_data("API_2", 2)
    
    # Using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(fetch_data, "API_1", 3)
        executor.submit(fetch_data, "API_2", 2)

    # Using threading.Thread
    thread1 = threading.Thread(target=fetch_data, args=("API_1", 3))
    thread2 = threading.Thread(target=fetch_data, args=("API_2", 2))
    thread1.start()
    thread2.start()

    print("Worrker threads started, main thread continues...")
    
    # Wait for both threads to finish before moving the main script forward
    # Python safety mechanism: Even if join is not called, the main thread will wait for all non-daemon threads to finish before exiting.
    # This is only true for non-daemon threads.
    # If you create a daemon thread:
    # then Python may exit without waiting for it.
    # So the full rule is:
    # non-daemon threads: Python waits for them
    # daemon threads: Python does not wait for them

    thread1.join()
    thread2.join()
    print(f"Total time taken: {time.perf_counter() - start_time:.2f} seconds")
    print("Main thread finished execution.")
