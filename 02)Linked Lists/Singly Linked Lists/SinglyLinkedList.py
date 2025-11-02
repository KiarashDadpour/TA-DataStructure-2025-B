class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def get_size(self): 
        count = 0
        current = self.head
        while current:           
            count += 1           
            current = current.next
        return count

    def is_empty(self):
        return self.head is None 

    def traversal(self):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        while current:
            print(current.get_info(),end="  ")
            current = current.next
        print()
        
    def search_node(self, value):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        found = False
        while (found is False) and (current is not None):
            if current.info == value:
                found = True
                return current
            else:
                current = current.next
        return current 

    def insert_head(self, new: Node):
        if self.head is None:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head = new  

    def insert_tail(self, new: Node):
        if self.head is None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new  

    def insert_after_node(self, new: Node, after: Node):
        if self.is_empty():
            self.head = new 
        else:
            current = self.head 
            while current:
                if current.info == after.info:
                    new.next = current.next
                    current.next = new
                    return 
                current = current.next  

    def delete_head(self):
        if self.is_empty():
            return "Empty List!!!"
        elif self.head == self.tail:  
            self.head = self.tail = None 
        else:
            current = self.head 
            self.head = self.head.next
            current.next = None 

    def deletd_tail(self):
        if self.is_empty():
            return "Empty List!!!"
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current


    def delete_after(self, after: Node):
        if self.is_empty():
            return "Empty List!!!"

        current = self.head
        while current:
            if current.info == after.info:
                to_delete = current.next
                if to_delete is None:
                    return "No node to delete after the given node."
                current.next = to_delete.next
                if to_delete == self.tail:  
                    self.tail = current
                to_delete.next = None
                return f"The node deleted."
            current = current.next
        return "Node not found!"


