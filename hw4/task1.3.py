from os import getpid
from multiprocessing import Process, Queue

def worker(q):
    message = q.get()
    print(f"Процесс PID={getpid()} получил сообщение: {message}")

if __name__ == "__main__":
    queue = Queue()
    p = Process(target=worker, args=(queue,))
    p.start()

    queue.put("Hello world!")
    p.join()