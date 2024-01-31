class Node:
    # create a constructor

    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:

    #function to initalize head
    def __init__(self):
        self.head = None

    #function to reverse the linked list
    def reverse(self):
        prev= None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            current = next
        self.head = prev

    #function to insert a new node 
    def push(self, new_nodedata):
        new_nodedata = Node(new_nodedata)
        new_nodedata.next = self.head
        self.head - new_nodedata



        
        


# def linkedList(a.value, a.node):

#     num = a.value
#     next = num.node
#     b = num.next

#     # prev = null

#     num = prev

#     b = num



# def linkedList(num, value, node):
     
#     num = a.value
#     next = num.node
#     b = next.value

#     prev = null

#     num.next  = prev

#     prev = nu

#     num =

