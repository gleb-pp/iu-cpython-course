from multiprocessing import Process, Pipe

def worker_receiver(conn):
    number = conn.recv()
    result = number ** 2
    conn.send(result)

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=worker_receiver, args=(child_conn,))
    p.start()
    parent_conn.send(5)
    result = parent_conn.recv()
    print(f"Квадрат числа: {result}")
    p.join()