import threading
import time
import random
from queue import Queue

inventario = {
    "notebook": 2500,
    "mouse": 50,
    "fone de ouvido": 70
}

fila_pedidos = Queue()

inventario_lock = threading.Lock()

def receber_pedidos():
    produtos = list(inventario.keys())
    for i in range(10):
        produto = random.choice(produtos)
        quantidade = random.randint(1, 5)
        pedido = {"id": i + 1, "produto": produto, "quantidade": quantidade}
        fila_pedidos.put(pedido)
        print(f"[Receber Pedidos] Pedido recebido: {pedido}")
        time.sleep(random.uniform(0.5, 1.5)) 

def processar_pedidos():
    while True:
        try:
            pedido = fila_pedidos.get(timeout=5) 
            produto = pedido["produto"]
            quantidade = pedido["quantidade"]

            with inventario_lock:
                if inventario[produto] >= quantidade:
                    print(f"[Processar Pedidos] Processando pedido {pedido['id']}: {quantidade} unidades de {produto}")
                    inventario[produto] -= quantidade
                else:
                    print(f"[Processar Pedidos] Pedido {pedido['id']} falhou: estoque insuficiente para {produto}")
            fila_pedidos.task_done()  
            time.sleep(random.uniform(0.8, 1.2))  
        except:
            break

def atualizar_inventario():
    while True:
        with inventario_lock:
            for produto, quantidade in inventario.items():
                reposicao = random.randint(1, 3)
                inventario[produto] += reposicao
                print(f"[Atualizar Inventário] Reabastecido {produto} com {reposicao} unidades (Total: {inventario[produto]})")
        time.sleep(5)  

def main():
    thread_receber = threading.Thread(target=receber_pedidos)
    thread_processar = threading.Thread(target=processar_pedidos)
    thread_atualizar = threading.Thread(target=atualizar_inventario, daemon=True)  # Daemon para encerrar ao final

    thread_receber.start()
    thread_processar.start()
    thread_atualizar.start()

    thread_receber.join()
    thread_processar.join()

    print("\n[Resultados Finais]")
    print("Inventário final:", inventario)

main()
