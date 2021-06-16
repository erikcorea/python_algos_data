###ARRAYS###
"""
new_list = [1,2,3]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
    if n == 1: 
        print(True)

        break
"""

###LINKED LIST###

class Node:

    #An object for storing a single node of a linked list.
    #Models two attribures - data and the link to the next node in the list
 

    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
 
   # Singly linked list


    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):

  
        #Returns the number of nodes in the list 
        #Takes 0(n) time
 

        current = self.head
        count = 0

        while current:
            count += 1 
            current = current.next_node

        return count

    def add(self, data):
    
       # Adds new node containing data at the head of the list
        #Takes 0(1) time(best)


        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
  
        #Search for the first node containing data that matches the key 
       # Return the node of `None` if not found

        #Takes O(n) time
 

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
   
        #Inserts a new Node containing data at index position
        #Insertion takes O(1) time but finding the node at the insertion point takes O(n) time.
        
        #Takes overall O(n) time  


        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

        while position > 1:
            current = node.next_node
            position -= 1

        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new
        new.next_node = next_node

    def remove(self, key):

       # Removes node containing data that matches the key
       # Returns the node or None if key doesn't exist
       # Takes O(n) time
   
         
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current


    def __repr__(self):

        #Return a string representation of the list.
        #Takes O(n) time.
   
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)


 
###MERGE SORT###
def merge_sort(list):
   
    #Sorts a list in ascending order
    #Returns a new sorted list

    #Divide: Find the midpoint of the list and divide into sublists
    #Conquer: Recursively sort the sublist created in previous step
    #Combine: Merge the sorted sublists created in previous step
   

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    #Divide the unsorted list at midpoint into sublist
    #Returns two sublist - left and right

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    #Merges two lists(arrays) sorting them in the process
    #Returns a new merged list

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [64,23,51,12,20,44,23]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))