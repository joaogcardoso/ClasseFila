from queue import Queue

class Fila:
    def __init__(self):
        self.items = Queue(maxsize = max)

    def inserir(self, item):

        if self.items.full():
            print("Erro! Limite atingido!")

        else:
            self.items.put(item)

    def remover(self):

        if self.items.empty():
            print("Erro! Lista vazia!")
        
        else:
            self.items.get()

    def mostrar(self):
        return self.items.queue
    
    def cheia(self):
        return self.items.full()
    
    def vazia(self):
        return self.items.empty()
    
    def tamanho(self):
        return self.items.qsize()
    
    def tamanho_maximo(self):
        return self.items.maxsize

try:
    max = int(input("Digite o tamanho máximo da lista: "))

    if max <= 0:
        print("Erro! Digite um número positivo")
        
    else:
        wrapper = Fila()

        while True:

            print("\nEscolha uma opção:")
            print("Opção 1: Inserir item na lista")
            print("Opção 2: Remover item da lista")
            print("Opção 3: Mostrar lista")
            print("Opção 4: Verificar se lista está cheia")
            print("Opção 5: Verificar se lista está vazia")
            print("Opção 6: Tamanho da lista")
            print("Opção 7: Tamanho máximo da lista")
            print("Opção 8: Sair\n")

            opcao = int(input("Digite uma opção: "))

            if opcao == 1:

                qnt = int(input("Quantos itens adicionar na lista? "))

                if qnt > max:
                    print(f"Erro! Limite de inserções é {max}")
                    break

                if qnt <= 0:
                    print("Erro! Digite um número positivo")

                else:
                    for i in range(0, qnt):
                        item = int(input(f"Digite o {i + 1}º item: "))
                        wrapper.inserir(item)
                        
                        if wrapper.cheia() == True:
                            break

            if opcao == 2:

                wrapper.remover()

            if opcao == 3:

                print(wrapper.mostrar())

            if opcao == 4:

                print(wrapper.cheia())

            if opcao == 5:

                print(wrapper.vazia())

            if opcao == 6:

                print(wrapper.tamanho())

            if opcao == 7:

                print(wrapper.tamanho_maximo())

            if opcao == 8:
                break

except ValueError:
    print(ValueError("Erro! Entrada inválida"))