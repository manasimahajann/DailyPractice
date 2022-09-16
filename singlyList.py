
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyList():
    def __init__(self):
        self.head = None 
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertToSingleLinkedList(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None 
                self.tail.next  = newNode
                self.tail = newNode
            else:
                index = 0
                tempNode = self.head
                while index < location-1:
                    tempNode = tempNode.next
                    index = index+1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    def traversalSLL(self):
        if self.head == None:
            print("LinkedList is empty")
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next

    def searchSLL(self, nodeVal):
        if self.head == None:
            print("LL does not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeVal:
                    return nodeVal
                else:
                    node = node.next
            return "value does not exist in this linkedlist"
    def deleteFromSLL(self, location):
        prevNode = None
        if self.head is None:
            print("sll does not exist")
        else:
            node = self.head
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.head = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.head = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index +1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteEntireSLL(self):
        if self.head is None:
            print("Single linkedlist is not a list")
        else:
            self.head = None
            self.tail = None

            # while node is not None:
            #     if node.value == nodeVal:
            #         if nodeVal == self.tail.value:
            #             self.tail == prevNode
            #         elif nodeVal == self.head:
            #             self.head == node.next
            #         else:
            #             nextNode = node.next
            #             prevNode.next = nextNode 
            #     else:
            #         prevNode = node
            #         node = node.next
            # return "value does not exist in this linkedlist"
# Node1 = Node(1)
# Node2 = Node(2)

# SinglyList = SinglyList()
# SinglyList.head = Node1

# SinglyList.head.next = Node2
# SinglyList.tail = Node2
SinglyList = SinglyList()
SinglyList.insertToSingleLinkedList(1,1)
SinglyList.insertToSingleLinkedList(2,1)
SinglyList.insertToSingleLinkedList(3,1)
SinglyList.insertToSingleLinkedList(4,1)
SinglyList.traversalSLL()
print(SinglyList.searchSLL(0)) 
print([node.value for node in SinglyList])
SinglyList.deleteFromSLL(3) 
SinglyList.deleteEntireSLL()
print([node.value for node in SinglyList])
