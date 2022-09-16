
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def createCSLL(self, nodeValue):
        node  = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        print("CircularSinglyLinkedList is created")

    def insertToSingleLinkedList(self, value, location):
        newNode = Node(value)
        if location == 0:
            if self.head == None:
                self.head = newNode
                self.tail.next = newNode
                newNode.next = self.head 
            else:
                                
                tempNode = self.head 
                while tempNode.next:
                    if tempNode.next == self.head:
                        tempNode.next = newNode
                    tempNode = tempNode.next
                # lastNode = tempNode.next
                # lastNode.next = newNode
                newNode.next = self.head
                self.head = newNode 
        elif location == -1:
            tempNode = self.head 
            while tempNode.next:
                if tempNode.next == self.head:
                    tempNode.next = newNode
                tempNode = tempNode.next
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode

        else:
            if self.head == self.tail:
                self.head.next = newNode
                newNode.next = self.tail
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index = index+1
                newNode.next = tempNode.next
                tempNode.next = newNode
    def traversalCLL(self, cl_list):
        if self.head == None:
            print("empty list")
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break

    def searchCLL(self, nodeVal):
        if self.head == None:
            print("empty list")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeVal:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "node does not exist in the list"



    def deleteNode(self, location = -1):
            if self.head is None:
                print("There is not any node in CSLL")
            else:
                # A node from beginning
                if location == 0:
                    # Only one node
                    if self.head == self.tail:
                        self.head.next = None
                        self.head = None
                        self.tail = None
                    # Multiple nodes
                    else:
                        self.head = self.head.next
                        self.tail.next = self.head
                elif location == -1:
                    # Only one node
                    if self.head == self.tail:
                        self.head.next = None
                        self.head = None
                        self.tail = None
                    # Multiple nodes
                    else:
                        node = self.head
                        while node is not None:
                            if node.next == self.tail:
                                break
                            node = node.next
                        node.next = self.head
                        self.tail = node
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    # we want to delete tempNode.next
                    nextNode = tempNode.next
                    tempNode.next = nextNode.next
                    # takes care of case where location == multiple of len(CSLL)
                    if nextNode == self.head:
                        self.head = tempNode.next

CircularSinglyLinkedList = CircularSinglyLinkedList()
CircularSinglyLinkedList.createCSLL(3)
print([node.value for node in CircularSinglyLinkedList])
print([node.value for node in CircularSinglyLinkedList])
CircularSinglyLinkedList.insertToSingleLinkedList(7, 1)

print([node.value for node in CircularSinglyLinkedList])

CircularSinglyLinkedList.insertToSingleLinkedList(8, -1) 
print([node.value for node in CircularSinglyLinkedList])
CircularSinglyLinkedList.insertToSingleLinkedList(4, 2)  
print([node.value for node in CircularSinglyLinkedList])
CircularSinglyLinkedList.insertToSingleLinkedList(9, 3)  
print([node.value for node in CircularSinglyLinkedList])
CircularSinglyLinkedList.insertToSingleLinkedList(2, 0)  
print([node.value for node in CircularSinglyLinkedList])
CircularSinglyLinkedList.traversalCLL(CircularSinglyLinkedList)
print([node.value for node in CircularSinglyLinkedList])
print(CircularSinglyLinkedList.searchCLL(1))

print([node.value for node in CircularSinglyLinkedList])
print([node.value for node in CircularSinglyLinkedList])

print(CircularSinglyLinkedList.deleteNode(-1))

print([node.value for node in CircularSinglyLinkedList])
