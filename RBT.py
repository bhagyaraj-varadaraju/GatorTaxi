# class RBNode:
#     def __init__(self, rideNumber=None, rideCost=None, tripDuration=None):
#         self.rideNumber = rideNumber
#         self.rideCost = rideCost
#         self.tripDuration = tripDuration
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.is_red = 1         # 1 for RED, 0 for BLACK
#         self.min_heap_node = None

# class RBTree:
#     def __init__(self):
#         self.root = None

#     def left_rotate(self, x):
#         y = x.right
#         x.right = y.left
#         if y.left != None:
#             y.left.parent = x
#         y.parent = x.parent
#         if x.parent == None:
#             self.root = y
#         elif x == x.parent.left:
#             x.parent.left = y
#         else:
#             x.parent.right = y
#         y.left = x
#         x.parent = y

#     def right_rotate(self, x):
#         y = x.left
#         x.left = y.right
#         if y.right != None:
#             y.right.parent = x
#         y.parent = x.parent
#         if x.parent == None:
#             self.root = y
#         elif x == x.parent.right:
#             x.parent.right = y
#         else:
#             x.parent.left = y
#         y.right = x
#         x.parent = y

#     def insert(self, node):
#         new_node = RBNode(node.rideNumber, node.rideCost, node.tripDuration)
#         y = None
#         x = self.root
#         while x != None:
#             y = x
#             if new_node.rideNumber < x.rideNumber:
#                 x = x.left
#             else:
#                 x = x.right
#         new_node.parent = y
#         if y == None:
#             self.root = new_node
#         elif new_node.rideNumber < y.rideNumber:
#             y.left = new_node
#         else:
#             y.right = new_node
#         new_node.left = None
#         new_node.right = None
#         new_node.is_red = 1
#         self.insert_fixup(new_node)

#     def insert_fixup(self, node):
#         while node.parent != None and node.parent.is_red == 1:
#             if node.parent == node.parent.parent.left:
#                 y = node.parent.parent.right
#                 if y != None and y.is_red == 1:
#                     node.parent.is_red = 0
#                     y.is_red = 0
#                     node.parent.parent.is_red = 1
#                     node = node.parent.parent
#                 else:
#                     if node == node.parent.right:
#                         node = node.parent
#                         self.left_rotate(node)
#                     node.parent.is_red = 0
#                     node.parent.parent.is_red = 1
#                     self.right_rotate(node.parent.parent)
#             else:
#                 y = node.parent.parent.left
#                 if y != None and y.is_red == 1:
#                     node.parent.is_red = 0
#                     y.is_red = 0
#                     node.parent.parent.is_red = 1
#                     node = node.parent.parent
#                 else:
#                     if node == node.parent.left:
#                         node = node.parent
#                         self.right_rotate(node)
#                     node.parent.is_red = 0
#                     node.parent.parent.is_red = 1
#                     self.left_rotate(node.parent.parent)
#         self.root.is_red = 0

#     def find_node(self, rideNumber):
#             """
#             Returns the node with the given rideNumber, or None if it does not exist.
#             """
#             x = self.root
#             while x is not None:
#                 if rideNumber == x.rideNumber:
#                     return x
#                 elif rideNumber < x.rideNumber:
#                     x = x.left
#                 else:
#                     x = x.right
#             return None

#     def delete(self, z):
#         """
#         Deletes node z from the tree.
#         """
#         # If the node to delete is a leaf, just remove it
#         if z.left is None and z.right is None:
#             if z.parent is None:  # z is the root
#                 self.root = None
#             elif z == z.parent.left:
#                 z.parent.left = None
#             else:
#                 z.parent.right = None
#             return

#         # If z has only one child, replace z with that child
#         if z.left is None:
#             y = z.right
#             self.transplant(z, y)
#         elif z.right is None:
#             y = z.left
#             self.transplant(z, y)
#         else:
#             # If z has two children, find its successor and replace z with it
#             y = self.tree_minimum(z.right)
#             if y.parent != z:
#                 self.transplant(y, y.right)
#                 y.right = z.right
#                 y.right.parent = y
#             self.transplant(z, y)
#             y.left = z.left
#             y.left.parent = y

#         # Fix the RB properties violated by the deletion
#         if y.is_red == 0:
#             self.delete_fixup(y)

#     def delete_fixup(self, x):
#         """
#         Fixes the RB properties that might have been violated by the deletion of a black node.
#         """
#         while x != self.root and x.is_red == 0:
#             if x == x.parent.left:
#                 w = x.parent.right
#                 if w.is_red == 1:
#                     w.is_red = 0
#                     x.parent.is_red = 1
#                     self.left_rotate(x.parent)
#                     w = x.parent.right
#                 if w.left.is_red == 0 and w.right.is_red == 0:
#                     w.is_red = 1
#                     x = x.parent
#                 else:
#                     if w.right.is_red == 0:
#                         w.left.is_red = 0
#                         w.is_red = 1
#                         self.right_rotate(w)
#                         w = x.parent.right
#                     w.is_red = x.parent.is_red
#                     x.parent.is_red = 0
#                     w.right.is_red = 0
#                     self.left_rotate(x.parent)
#                     x = self.root
#             else:
#                 w = x.parent.left
#                 if w.is_red == 1:
#                     w.is_red = 0
#                     x.parent.is_red = 1
#                     self.right_rotate(x.parent)
#                     w = x.parent.left
#                 if w.right.is_red == 0 and w.left.is_red == 0:
#                     w.is_red = 1
#                     x = x.parent
#                 else:
#                     if w.left.is_red == 0:
#                         w.right.is_red = 0
#                         w.is_red = 1
#                         self.left_rotate(w)
#                         w = x.parent.left
#                     w.is_red = x.parent.is_red
#                     x.parent.is_red = 0
#                     w.left.is_red = 0
#                     self.right_rotate(x.parent)
#                     x = self.root
#         x.is_red = 0

#     def transplant(self, u, v):
#         """
#         Replaces the subtree rooted at node u with the subtree rooted at node v.
#         """
#         if u.parent is None:
#             self.root = v
#         elif u == u.parent.left:
#             u.parent.left = v
#         else:
#             u.parent.right = v
#         if v != None:
#             v.parent = u.parent


# Define Node
class RBNode():
    # def __init__(self,val):
    #     self.val = val                                   # Value of Node
    #     self.parent = None                               # Parent of Node
    #     self.left = None                                 # Left Child of Node
    #     self.right = None                                # Right Child of Node
    #     self.color = 1                                   # Red Node as new node is always inserted as Red Node

    def __init__(self, rideNumber, rideCost, tripDuration, min_heap_node=None):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1         # 1 for RED, 0 for BLACK
        self.min_heap_node = min_heap_node

    def __str__(self):
        return f"RBNode = ({self.rideNumber}, {self.rideCost}, {self.tripDuration}, HEAPptr = {'Exists' if self.min_heap_node else 'None'})"

    def __repr__(self):
        return self.__str__()

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = RBNode (0, 0, 0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    # Insert New Node
    def insert(self, z):
        node = RBNode(z.rideNumber, z.rideCost, z.tripDuration, z.min_heap_node)
        node.parent = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red

        y = None
        x = self.root

        while x != self.NULL :                           # Find position for new node
            y = x
            if node.rideNumber < x.rideNumber :
                x = x.left
            else :
                x = x.right

        node.parent = y                                  # Set parent of Node as y
        if y == None :                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.rideNumber < y.rideNumber :                          # Check if it is right Node or Left Node by checking the value
            y.left = node
        else :
            y.right = node

        if node.parent == None :                         # Root node is always Black
            node.color = 0
            return

        if node.parent.parent == None :                  # If parent of node is Root Node
            return

        self.fixInsert ( node )                          # Else call for Fix Up

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    # Code for left rotate
    def LR ( self , x ) :
        y = x.right                                      # Y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y

    # Code for right rotate
    def RR ( self , x ) :
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If x is root node
            self.root = y                                # Set y as root
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix Up Insertion
    def fixInsert(self, k):
        while k.parent.color == 1:                        # While parent is red
            if k.parent == k.parent.parent.right:         # if parent is right child of its parent
                u = k.parent.parent.left                  # Left child of grandparent
                if u.color == 1:                          # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # Set grandparent node as Red
                    k = k.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:                # If k is left child of it's parent
                        k = k.parent
                        self.RR(k)                        # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:                                         # if parent is left child of its parent
                u = k.parent.parent.right                 # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # set color of grandparent as Red
                    k = k.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:               # if k is right child of its parent
                        k = k.parent
                        self.LR(k)                        # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)              # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                break
        self.root.color = 0                               # Set color of root as black

    # Function to fix issues after deletion
    def fixDelete ( self , x ) :
        while x != self.root and x.color == 0 :           # Repeat until x reaches nodes and color of x is black
            if x == x.parent.left :                       # If x is left child of its parent
                s = x.parent.right                        # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.parent.color = 1                    # Make its parent red
                    self.LR ( x.parent )                  # Call for left rotate on parent of x
                    s = x.parent.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                           # Set color of s as red
                    x = x.parent
                else :
                    if s.right.color == 0 :               # If right child of s is black
                        s.left.color = 0                  # set left child of s as black
                        s.color = 1                       # set color of s as red
                        self.RR ( s )                     # call right rotation on x
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0                    # Set parent of x as black
                    s.right.color = 0
                    self.LR ( x.parent )                  # call left rotation on parent of x
                    x = self.root
            else :                                        # If x is right child of its parent
                s = x.parent.left                         # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.parent.color = 1                    # Make its parent red
                    self.RR ( x.parent )                  # Call for right rotate on parent of x
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.parent
                else :
                    if s.left.color == 0 :                # If left child of s is black
                        s.right.color = 0                 # set right child of s as black
                        s.color = 1
                        self.LR ( s )                     # call left rotation on x
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RR ( x.parent )
                    x = self.root
        x.color = 0

    # Function to transplant nodes
    def __rb_transplant ( self , u , v ) :
        if u.parent == None :
            self.root = v
        elif u == u.parent.left :
            u.parent.left = v
        else :
            u.parent.right = v
        v.parent = u.parent

    # Function to handle deletion
    def delete_node_helper ( self , node, ride_number ) :
        z = self.find_node_test(self.root, ride_number)

        # while node != self.NULL :                          # Search for the node having that value/ key and store it in 'z'
        #     if node.rideNumber == ride_number :
        #         z = node

        #     if node.rideNumber < ride_number :
        #         node = node.right
        #     else :
        #         node = node.left

        if not z :                                # If Key is not present then deletion not possible so return
            print ( "Value not present in Tree !!" )
            return

        y = z
        y_original_color = y.color                          # Store the color of z- node
        if z.left == self.NULL :                            # If left child of z is NULL
            x = z.right                                     # Assign right child of z to x
            self.__rb_transplant ( z , z.right )            # Transplant Node to be deleted with x
        elif (z.right == self.NULL) :                       # If right child of z is NULL
            x = z.left                                      # Assign left child of z to x
            self.__rb_transplant ( z , z.left )             # Transplant Node to be deleted with x
        else :                                              # If z has both the child nodes

            y = self.minimum ( z.right )                    # Find minimum of the right sub tree
            y_original_color = y.color                      # Store color of y
            x = y.right
            if y.parent == z :                              # If y is child of z
                x.parent = y                                # Set parent of x as y
            else :
                self.__rb_transplant ( y , y.right )
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant ( z , y )
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0 :                          # If color is black then fixing is needed
            self.fixDelete ( x )

    # Deletion of node
    def delete ( self , rideNumber ) :
        self.delete_node_helper ( self.root, rideNumber )         # Call for deletion

    def find_node(self, rideNumber):
        """
        Returns the node with the given rideNumber, or None if it does not exist.
        """
        z = None
        node = self.root
        while node != self.NULL:
            if rideNumber == node.rideNumber:
                z = node
            elif rideNumber < node.rideNumber:
                node = node.left
            else:
                node = node.right
        return z


    def find_node_test(self, node, ride_number):
        if node is None:
            return

        ## Found the node with the ride_number
        if node.rideNumber == ride_number:
            return node

        if node.rideNumber < ride_number:
            ## If current node is less than the ride_number, search in right subtree
            return self.find_node_test(node.right, ride_number)
        else:
             ## If the current node is greater than the ride_number, search in left subtree.
            return self.find_node_test(node.left, ride_number)

    def search(self, ride_number):
        node = self.find_node_test(self.root, ride_number)
        print(node)
        return node


    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.rideNumber ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )
