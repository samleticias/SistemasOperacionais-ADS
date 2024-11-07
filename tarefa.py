import psutil
import subprocess
import time

def iniciaProcesso():
   processo = subprocess.Popen(["firefox"]) 
   return processo

def monitoraProcesso(pid_alvo):
   try:
       proc = psutil.Process(pid_alvo)
       print(f"Monitorando processo com PID {pid_alvo}...\n")

       while True:
           if proc.is_running():
               status = proc.status()
               cpu_percent = proc.cpu_percent(interval=1)
               memoria = proc.memory_info().rss / (1024 ** 2)

               print(f"Status: {status} | CPU: {cpu_percent}% | Memória: {memoria:.2f} MB")
           else:
               print(f"O processo PID {pid_alvo} foi finalizado.")
               break
           time.sleep(2)
   except psutil.NoSuchProcess:
       print(f"O processo PID {pid_alvo} não foi encontrado.")
   except psutil.AccessDenied:
       print(f"Sem permissão para acessar o processo PID {pid_alvo}.")

def main():
   print("Iniciando o processo...\n")
   processo = iniciaProcesso()

   monitoraProcesso(processo.pid)

main()