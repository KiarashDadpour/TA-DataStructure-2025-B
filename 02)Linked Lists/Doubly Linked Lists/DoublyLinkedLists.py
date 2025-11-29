class Node:
    def __init__(self, info=None, next=None, prev=None):
        self.info = info
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.info)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after_node(self, target, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current:
                if current.info == target:
                    new_node = Node(data)
                    new_node.next = current.next
                    new_node.prev = current
                    if current.next:
                        current.next.prev = new_node
                    else:  
                        self.tail = new_node
                    current.next = new_node
                    return
                current = current.next
            print(f"Node with data {target} does not exist.")

    def delete_head(self):
        if not self.head:
            print("List is empty. cannot delete head.")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_tail(self):
        if not self.head:
            print("LEmpty List!!!)
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_after(self, target_data):
        if not self.head:
            print("Empty List!!!")
            return

        current = self.head
        while current:
            if current.info == target_data:
                node_to_delete = current.next

                if not node_to_delete:
                    print("No node to delete after the given node.")
                    return None

                current.next = node_to_delete.next
                if node_to_delete.next:
                    node_to_delete.next.prev = current
                else:
                    self.tail = current
                print("The node deleted.")
                return

            current = current.next

        print("Node not found!")

    def search_node(self, data):
        current = self.head
        while current:
            if current.info == data:
                return True
            current = current.next
        return False

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def traversal(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        elements = []
        while current:
            elements.append(current.info)
            current = current.next

        print(" <--> ".join(map(str, elements)))
