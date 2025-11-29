class Node:
    def __init__(self, info):
        self.info = int(info)
        self.next = None
        
    def get_info(self):
        return self.info


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



def create_linked_list_from_number(number_str):
    ll = LinkedList()
    for digit in reversed(number_str):
        ll.insert_tail(Node(int(digit)))
    return ll

def add_big_numbers(ll1: LinkedList, ll2: LinkedList):
    result = LinkedList()
    n1 = ll1.head
    n2 = ll2.head
    carry = 0
    
    while n1 or n2 or carry:
        digit1 = n1.info if n1 else 0
        digit2 = n2.info if n2 else 0
        
        total = digit1 + digit2 + carry
        carry = total // 10
        result.insert_tail(Node(total % 10))
        
        if n1: n1 = n1.next
        if n2: n2 = n2.next
    
    return result

def print_linked_list_number(ll: LinkedList):
    digits = []
    current = ll.head
    while current:
        digits.append(str(current.info))
        current = current.next
    print("".join(reversed(digits)))


num1 = "98345345435345435457634523543453534534553435453454354321987654324655341546546456425346545698765345436434321"
num2 = "12343453345345233424556789123345234352343254323534542345234456789145343254634632464564654624623454352536789"

ll1 = create_linked_list_from_number(num1)
ll2 = create_linked_list_from_number(num2)

result = add_big_numbers(ll1, ll2)

print("Result:")
print_linked_list_number(result)

