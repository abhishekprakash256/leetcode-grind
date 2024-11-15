"""
Make a dubly linked list and operations 
"""



class Node:
    def __init__(self,val = None,prev = None,next = None):
        self.val = val
        self.next = next 
        self.prev = prev


class Double_list():

    def __init__(self):

        self.head = None
        self.tail = None
    
    def set_head(self,val):
        """
        The function to set the head 
        """
        #make node 
        node = Node(val)

        if self.head :

            node.next = self.head

            self.head.prev = node

            self.head = node

            return "head is set"
        
        self.head = node

        return "head is set"
    

    def set_tail(self,val):
        """
        the function to set the tail of the list
        """

        node = Node(val)

        if self.tail:

            self.tail.next = node

            node.prev = self.tail

            self.tail = node

            return  "Tail is set"


        self.head.next = node
        node.prev = self.head
        self.tail = node

        return "Tail is set"
        

    
    def add_node(self,val):
        """
        The function to set the node 
        """

        if not self.head :

            self.set_head(val)

            return "Node is set"
        

        if not self.tail : 

            self.set_tail(val)

            return "Node is set"
        
        #make the node 
        node = Node(val)
        
        prev_temp = self.tail.prev

        next_temp = self.tail

        prev_temp.next = node
        node.prev = prev_temp

        node.next = next_temp
        next_temp.prev = node

        self.tail = next_temp


        return "Node is set"


    def remove_node(self,val):
        """
        remove the node as per val
        """

        if self.head.val == val:

            if self.head.next : 
                
                self.head = self.head.next
                self.head.prev = None
            
            else:

                self.head = None
            
            return "Node is removed as head node"
        

        if self.tail.val == val:

            if self.tail.prev :

                self.tail = self.tail.prev
                self.tail.next = None
            
            else:

                self.tail = None
            

            return "Node is removed as tail node"
        

        temp = self.head

        while temp.val != val : 

            temp = temp.next

        
        #remove the node 

        prev_temp = temp.prev
        next_temp = temp.next

        temp.prev = prev_temp
        temp.next = next_temp

        prev_temp.next = next_temp
        next_temp.prev = prev_temp

        return "Node is removed"




    

    def print_list_head(self):
        """
        The fucntion to print the list 
        """

        temp = self.head 

        while temp:

            print(temp.val)

            temp = temp.next
        

        return "The list is printed"
    

    def print_list_tail(self):
        """
        The function to print the list from tail
        """

        temp = self.tail

        while temp:

            print(temp.val)

            temp = temp.prev
            
        return "The list is printed"




#make the node and test 
doublelist = Double_list()
doublelist.add_node(1)
doublelist.add_node(5)
doublelist.add_node(2)
doublelist.add_node(3)
doublelist.add_node(4)



doublelist.print_list_head()

doublelist.remove_node(3)

doublelist.print_list_tail()