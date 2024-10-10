import threading

def print_cube(num: int):
    print(f"Cube: {num**3}")

def print_square(num: int):
    print(f"Square: {num**2}")

if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    
    # To start a thread, we use the start() method of the Thread class.

    t1.start()
    t2.start()

    # Once the threads start, the current program (you can think of
    # it like a main thread) also keeps on executing. In order to
    # stop the execution of the current program until a thread is
    # complete, we use the join() method.

    t1.join()
    t2.join()

    # The current program will first wait for the completion of t1
    # and then t2. Once, they are finished, the remaining statements
    # of the current program are executed.

    print("Done!")
