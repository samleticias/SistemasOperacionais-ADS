import threading
import time

def executar_tarefa(nome_thread, tempo_espera):
    for i in range(5):
        print(f"{nome_thread} - contador {i + 1}")
        time.sleep(tempo_espera)
    print(f"{nome_thread} terminou")

def main():
    thread1 = threading.Thread(target=executar_tarefa, args=("Thread 1", 1))
    thread2 = threading.Thread(target=executar_tarefa, args=("Thread 2", 1.5))
    thread3 = threading.Thread(target=executar_tarefa, args=("Thread 3", 2))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("\ntodas as threads foram concluídas ...\n")

main()