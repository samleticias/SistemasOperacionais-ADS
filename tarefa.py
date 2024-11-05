import psutil
import time
import os
import subprocess
import threading

uso_cpu = 0.0
uso_memoria = 0.0

# funcao para monitorar o uso de CPU e memória do bloco de notas
def monitorar_notepad(pid):
    global uso_cpu, uso_memoria
    try:
        proc = psutil.Process(pid)
        while proc.is_running():
            uso_cpu = proc.cpu_percent(interval=1)
            uso_memoria = proc.memory_percent()
            time.sleep(1)
    except psutil.NoSuchProcess:
        print("[Monitoramento] processo não encontrado.")

# funcao para menu de controle do bloco de notas
def menu_controle(pid):
    opcao = ""
    while opcao != "4":
        print("\n|--------- menu de controle ---------|")
        print("> 1 - verificar se o bloco de notas está rodando")
        print("> 2 - mostrar uso de CPU e memória")
        print("> 3 - encerrar o bloco de notas")
        print("> 4 - voltar ao menu principal")
        opcao = input("escolha uma opção: ")

        if opcao == "1":
            if psutil.pid_exists(pid) and psutil.Process(pid).is_running():
                print("\nbloco de notas está rodando ...\n")
            else:
                print("\nbloco de notas não está rodando ...\n")
        
        elif opcao == "2":
            # mostra uso de CPU e memória do último monitoramento
            print(f"\n[Estado] Uso de CPU: {uso_cpu}% | Uso de Memória: {uso_memoria}%")
        
        elif opcao == "3":
            # encerra tarefa de bloco de notas
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                print("\nbloco de notas foi encerrado ...\n")
            except psutil.NoSuchProcess:
                print("\nbloco de notas já foi encerrado!\n")

        elif opcao != "4":
            print("\nopção inválida!\n")

def menu():
    opcao = ""
    while opcao != "0":
        print("\n|------------ menu ------------|")
        print("> 1 - criar arquivo e abrir no bloco de notas")
        print("> 0 - sair")
        opcao = input("escolha uma opção: ")

        if opcao == "1":
            nome_arquivo = input("\ndigite o nome do arquivo (exemplo: arquivo.txt): ")
            conteudo = input("\ndigite o conteúdo a ser escrito no arquivo: ")

            with open(nome_arquivo, "w") as arquivo:
                arquivo.write(conteudo)
            print(f"\nescrita no arquivo {nome_arquivo} realizada com sucesso!\n")

            # abrir o bloco de notas
            notepad_process = subprocess.Popen(["notepad.exe", nome_arquivo])

            threading.Thread(target=monitorar_notepad, args=(notepad_process.pid,), daemon=True).start()

            # mostra menu de controle para monitoramento
            menu_controle(notepad_process.pid)

        elif opcao != "0":
            print("\nopção inválida!\n")
    
    print('\nsaindo ...\n')

if __name__ == "__main__":
    menu()
