class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class LinkedListIterator:
    def __init__(self, linkedList):
        self.linkedList = linkedList
        # to keep track of the iterator
        self._currentNode = self.linkedList.head

    def __next__(self):
        if self._currentNode is None:
            raise StopIteration
        else:
            response = self._currentNode
            self._currentNode = self._currentNode.next
            return response


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count

    def __iter__(self):
        return LinkedListIterator(self)

    def __str__(self) -> str:
        text = ''
        for n in l:
            text += str(n) + ' -> '

        return text

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert(self, index, data):
        if index < 0 or index >= len(self):
            raise Exception('Invalid Index')

        if index == len(self):
            self.append(data)
            return

        for count, node in enumerate(self):
            if count == index - 1:
                node.next = Node(data, node.next)
                break

    def insert_after(self, value, data):
        for node in self:
            if node.data == value:
                node.next = Node(data, node.next)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1

        for count, node in enumerate(self):
            if count == index - 1:
                to_replace = node.next.next
                del(node.next)
                node.next = to_replace
                break

    def remove(self, value):
        for node in self:
            if node.next.data == value:
                to_replace = node.next.next
                del(node.next)
                node.next = to_replace
                break

if __name__ == '__main__':
    print('-.- Linked List Example -.-')

    l = LinkedList()

    l.append('first')
    l.append('second')
    l.append('third')
    l.append('fourth')
    l.append('fifth')

    print('initial linked list: ')
    print(l)

    l.insert(2, 'inserted')
    print('-'*50+'\nafter insertion: ')
    print(l)

    l.pop()
    l.pop(2)
    print('-'*50+'\nafter pop: ')
    print(l)

    l.remove('second')
    print('-'*50+'\nafter remove: ')
    print(l)

    l.insert_after('first', 'second')
    print('-'*50+'\nafter insert after: ')
    print(l)

    print('-'*50+'\nlinked list length: ')
    print(len(l))
