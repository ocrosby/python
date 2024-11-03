"""
A thread pool is a collection of threads that are created in advance and
can be reused to execute multiple tasks. The concurrent.futures module
in Python provides a ThreadPoolExecutor class that makes it easy to
create and manage a thread pool.

In this example, we define a function worker that will run in a thread.
We create a ThreadPoolExecutor with a maximum of 2 worker threads. We then
submit two tasks to the pool using the submit method. The pool manages the
execution of the tasks in its worker threads. We use the shutdown method
to wait for all tasks to complete before the main thread continues.

Multithreading can help you make your programs more efficient and responsive.
However, it’s important to be careful when working with threads to avoid
issues such as race conditions and deadlocks.

This code uses a thread pool created with concurrent.futures.ThreadPoolExecutor
to run two worker tasks concurrently. The main thread waits for the worker
threads to finish using pool.shutdown(wait=True) . This allows for efficient
parallel processing of tasks in a multi-threaded environment.
"""

import concurrent.futures

def worker():
    print("Worker thread running")

if __name__ == "__main__":
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    pool.submit(worker)
    pool.submit(worker)

    pool.shutdown(wait=True)

    print("Main thread continuing to run")
