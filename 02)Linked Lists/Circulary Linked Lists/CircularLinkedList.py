
class Node:
    def __init__(self, info=None, next=None) -> None:
        self.info = info
        self.next = next

    def __str__(self) -> str:
        return str(self.info)


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next

            new_node.next = self.head
            tail.next = new_node
            self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next

            tail.next = new_node
            new_node.next = self.head

    def insert_after_node(self, target, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while True:
                if current.info == target:
                    new_node = Node(data)
                    new_node.next = current.next
                    current.next = new_node
                    return

                current = current.next
                if current == self.head:
                    break
            print(f"Node with data {target} does not exist.")

    def delete_head(self):
        if not self.head:
            print("List is empty. cannot delete head.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next

            tail.next = self.head.next
            self.head = self.head.next

    def delete_tail(self):
        if not self.head:
            print("List is empty. connot delete tail")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next

            current.next = self.head

    def delete_after(self, target_data):
        if not self.head:
            print("Empty List!!!")
            return

        if self.head.next == self.head:
            print("No node to delete after the given node")
            return

        current = self.head
        while True:
            if current.info == target_data:
                node_to_delete = current.next

                if node_to_delete == self.head:
                    print("No node to delete after the given node.")
                    return

                if current.next.next == self.head and current == self.head:
                    current.next = self.head
                    print("The node deleted.")
                    return

                current.next = node_to_delete.next
                print("The node deleted.")
                return

            current = current.next
            if current == self.head:
                break

        print("Node not found!")

    def search_node(self, data):
        if not self.head:
            return False

        current = self.head
        while True:
            if current.info == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get_size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def traversal(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        elements = []
        while True:
            elements.append(current.info)
            current = current.next
            if current == self.head:
                break

        print(" -> ".join(map(str, elements)) + f" -> (back to {elements[0]})")
