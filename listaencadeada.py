
#classe chamada Node para representar um nó na lista encadeada
#passamos o valor como argumento que será atribuido ao 'data' do objeto nó
#inicialmente, o nó não aponta para nenhum outro nó

class Node:
 def __init__(self, data):
    self.data = data
    self.next_node = None

#classe para representar a lista encadeada
#inicialmente, a lista encadeada está vazia e não tem nenhum nó
class LinkedList:
 def __init__(self):
    self.head = None


#método da classe 'LinkedList' para adicionar um novo nó ao final da lista encadeada
#um novo objeto é criado e a lista verifica se está vazia. Se estiver vazia, o atributo 'head'
#é atualizado para apontar para o novo nó. Se não estiver vazia, um loop é usado para encontrar
#o último nó na lista, percorrendo até encontrar o último nó. Quando é encontrado, seu atributo
#é atualizado para apontar para o novo nó, inserindo no final da lista
 def append(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
    else:
        current = self.head
        while current.next_node:
            current = currennt.next_node
        current.next_node = new_node

#imprime os valores dos nós na lista encadeada
 def print_list(self):
    current = self.head
    while current:
        print (current.data, end =" -> ")
        current = current.next_node
    print ("None")

#conta número de nós na lista
#começa a partir do nó da cabeça, incrementando count a cada nó encontrado na lista e no fim, 
#retorna o numero total
def count_nodes(linked_list):
    count = 0
    current = linked_list.head
    while current:
        count += 1
        current = current.next_node
    return count
