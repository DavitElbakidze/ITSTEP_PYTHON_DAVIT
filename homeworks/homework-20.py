class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head = Node(value)
        else:
            self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self):
        if self.head is None:
            raise Exception("Cannot remove from an empty linked list")
        current = self.head
        if current.next is None:
            self.head = None
            return
        while current.next.next:
            current = current.next
        current.next = None

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)

    print("Linked list before removal:")
    current = linked_list.head
    while current:
        print(current.value)
        current = current.next

    linked_list.remove()

    print("Linked list after removal:")
    current = linked_list.head
    while current:
        print(current.value)
        current = current.next

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Popping elements from the stack:")
    while not stack.is_empty():
        print(stack.pop())
