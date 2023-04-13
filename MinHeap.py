class MinHeapNode:
    def __init__(self, rideNumber, rideCost, tripDuration, rbt_node=None):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration
        self.rbt_node = rbt_node

    def __str__(self):
        return f"MinHeapNode = ({self.rideNumber}, {self.rideCost}, {self.tripDuration}, RBTptr = {'Exists' if self.rbt_node else 'None'})"

    def __repr__(self):
        return self.__str__()

class MinHeap:
    def __init__(self):
        # Initialize an empty heap and a dictionary to store nodes and their indices in the heap
        self.heap = []
        self.node_map = {}

    # Calculate parent index
    @staticmethod
    def parent(i):
        return (i - 1) // 2

    # Calculate left child index
    @staticmethod
    def left(i):
        return 2 * i + 1

    # Calculate right child index
    @staticmethod
    def right(i):
        return 2 * i + 2

    # Insert a new node into the heap
    def insert(self, node):
        # Append the node to the end of the heap
        self.heap.append(node)

        # Add the node to the node_map with its index as the value
        self.node_map[node] = len(self.heap) - 1

        # Move the appended node up the heap if its value is less than its parent's value
        self.bubble_up(len(self.heap) - 1)

    # Heapify the heap starting from node i downwards
    def heapify(self, i):
        smallest = i
        # Check and assign smallest to the index among the current, left and right
        l, r = self.left(i), self.right(i)
        if l < len(self.heap) and self.is_less_than(l, smallest):
            smallest = l
        if r < len(self.heap) and self.is_less_than(r, smallest):
            smallest = r

        # If the value of node i is not the smallest, swap it with the smallest child node
        if smallest != i:
            self.swap_nodes(i, smallest)
            # Continue heapify operation until the current node is the smallest among current, left and right
            self.heapify(smallest)

    # Extract the minimum node from the heap
    def extract_min(self):
        if len(self.heap) == 0:
            return None

        # Get the root node (minimum value) of the heap
        root = self.heap[0]
        del self.node_map[root]

        if len(self.heap) > 1:
            # Replace the root node with the last node in the heap and heapify
            self.heap[0] = self.heap.pop()
            self.node_map[self.heap[0]] = 0
            self.heapify(0)
        else:
            # If the heap contains only one node, remove it from the heap
            self.heap.pop()
        return root

    # Delete an arbitrary node from the heap
    def delete_node(self, node):
        if node not in self.node_map:
            return

        i = self.node_map[node]
        del self.node_map[node]

        # If the node is the last element in the heap, pop it
        if i == len(self.heap) - 1:
            self.heap.pop()

        # Otherwise replace the node with the last element in the heap
        else:
            self.heap[i] = self.heap.pop()
            self.node_map[self.heap[i]] = i

            # Heapify or bubble-up as necessary
            if self.is_less_than(i, self.parent(i)):
                self.bubble_up(i)
            else:
                self.heapify(i)

    # Compare the rideCost of the two nodes
    def is_less_than(self, i, j):
        # Return true if the rideCost of i is smaller than the rideCost of j
        if self.heap[i].rideCost < self.heap[j].rideCost:
            return True

        # If the rideCost of i and j is same, break the tie using tripDuration
        elif self.heap[i].rideCost == self.heap[j].rideCost:
            return self.heap[i].tripDuration < self.heap[j].tripDuration
        return False

    # Swap the nodes at the given indices
    def swap_nodes(self, i, j):
        self.node_map[self.heap[i]] = j
        self.node_map[self.heap[j]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Move up the heap until its parent node is smaller than itself
    def bubble_up(self, i):
        while i > 0 and self.is_less_than(i, self.parent(i)):
            self.swap_nodes(i, self.parent(i))
            i = self.parent(i)

    # To print the heap
    def print_heap(self):
        print(self.heap)

    # To update the given node with new info
    def update_heap_node(self, node, new_cost, new_duration):
        if node not in self.node_map:
            return

        # Update rideCost and tripDuration
        node.rideCost = new_cost
        node.tripDuration = new_duration

        i = self.node_map[node]
        # If the current node is the root of the heap, heapify it
        if i == 0:
            self.heapify(i)

        # Bubble up if the current node is smaller than its parent
        elif self.is_less_than(i, self.parent(i)):
            self.bubble_up(i)

        # Otherwise heapify it
        else:
            self.heapify(i)
