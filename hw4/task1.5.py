from multiprocessing import Manager, Process, current_process
from os import getpid

def register_process(shared_dict):
    process_name = current_process().name
    pid = getpid()
    shared_dict[process_name] = (pid, "Данные записаны")

if __name__ == "__main__":
    manager = Manager()
    shared_dict = manager.dict()
    processes = []
    
    for i in range(3):
        p = Process(
            target=register_process,
            args=(shared_dict,),
            name=f"Process-{i+1}"
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for name, info in shared_dict.items():
        print(f"Процесс {name} (PID {info[0]}) записал: {info[1]}")