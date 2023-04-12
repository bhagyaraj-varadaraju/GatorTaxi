# class MinHeapNode:
#     def __init__(self, rideNumber, rideCost, tripDuration, rbt_node = None):
#         self.rideNumber = rideNumber
#         self.rideCost = rideCost
#         self.tripDuration = tripDuration
#         self.rbt_node = rbt_node

# class MinHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, i):
#         return (i - 1) // 2

#     def left(self, i):
#         return 2 * i + 1

#     def right(self, i):
#         return 2 * i + 2

#     def get_min(self):
#         if len(self.heap) == 0:
#             return None
#         return self.heap[0]

#     def insert(self, node):
#         self.heap.append(node)
#         i = len(self.heap) - 1
#         while i != 0 and self.heap[self.parent(i)].rideCost > self.heap[i].rideCost:
#             self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
#             i = self.parent(i)
#         while i != 0 and self.heap[self.parent(i)].rideCost == self.heap[i].rideCost and self.heap[self.parent(i)].tripDuration > self.heap[i].tripDuration:
#             self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
#             i = self.parent(i)

#     def heapify(self, i):
#         l = self.left(i)
#         r = self.right(i)
#         smallest = i
#         if l < len(self.heap) and self.heap[l].rideCost < self.heap[smallest].rideCost:
#             smallest = l
#         if l < len(self.heap) and self.heap[l].rideCost == self.heap[smallest].rideCost and self.heap[l].tripDuration < self.heap[smallest].tripDuration:
#             smallest = l
#         if r < len(self.heap) and self.heap[r].rideCost < self.heap[smallest].rideCost:
#             smallest = r
#         if r < len(self.heap) and self.heap[r].rideCost == self.heap[smallest].rideCost and self.heap[r].tripDuration < self.heap[smallest].tripDuration:
#             smallest = r
#         if smallest != i:
#             self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
#             self.heapify(smallest)

#     def extract_min(self):
#         if len(self.heap) == 0:
#             return None
#         root = self.heap[0]
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
#         self.heapify(0)
#         return root

#     def decrease_key(self, i, key):
#         self.heap[i].rideCost = key
#         while i != 0 and self.heap[self.parent(i)].rideCost > self.heap[i].rideCost:
#             self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
#             i = self.parent(i)
#         while i != 0 and self.heap[self.parent(i)].rideCost == self.heap[i].rideCost and self.heap[self.parent(i)].tripDuration > self.heap[i].tripDuration:
#             self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
#             i = self.parent(i)

#     def delete_node(self, node):
#         for i in range(len(self.heap)):
#             if self.heap[i] == node:
#                 self.decrease_key(i, float("-inf"))
#                 self.extract_min()
#                 return

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
        self.heap = []
        self.node_map = {}

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def insert(self, node):
        self.heap.append(node)
        self.node_map[node] = len(self.heap) - 1
        # print("MAP: ", self.node_map)
        self._bubble_up(len(self.heap) - 1)

    def heapify(self, i):
        smallest = i
        l, r = self.left(i), self.right(i)
        if l < len(self.heap) and self._is_less_than(l, smallest):
            smallest = l
        if r < len(self.heap) and self._is_less_than(r, smallest):
            smallest = r
        if smallest != i:
            self._swap_nodes(i, smallest)
            self.heapify(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        del self.node_map[root]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.node_map[self.heap[0]] = 0
            self.heapify(0)
        else:
            self.heap.pop()
        return root

    def decrease_key(self, node, new_cost):
        if new_cost >= node.rideCost:
            return
        node.rideCost = new_cost
        self._bubble_up(self.node_map[node])

    def increase_key(self, node, new_cost):
        if new_cost <= node.rideCost:
            return
        node.rideCost = new_cost
        self.heapify(self.node_map[node])

    def delete_node(self, node):
        if node not in self.node_map:
            return

        # print("MAP: ", self.node_map)
        i = self.node_map[node]
        del self.node_map[node]
        # print("MAP: ", self.node_map)
        if i == len(self.heap) - 1:
            self.heap.pop()
        else:
            self.heap[i] = self.heap.pop()
            self.node_map[self.heap[i]] = i
            if self._is_less_than(i, self.parent(i)):
                self._bubble_up(i)
            else:
                self.heapify(i)

    def _is_less_than(self, i, j):
        if self.heap[i].rideCost < self.heap[j].rideCost:
            return True
        elif self.heap[i].rideCost == self.heap[j].rideCost:
            return self.heap[i].tripDuration < self.heap[j].tripDuration
        return False

    def _swap_nodes(self, i, j):
        self.node_map[self.heap[i]] = j
        self.node_map[self.heap[j]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_up(self, i):
        while i > 0 and self._is_less_than(i, self.parent(i)):
            self._swap_nodes(i, self.parent(i))
            i = self.parent(i)

    def print_heap(self):
        print(self.heap)

    def update_trip_duration(self, node, new_duration):
        if node not in self.node_map:
            return
        node.tripDuration = new_duration
        i = self.node_map[node]
        if i == 0:
            self.heapify(i)
        elif self._is_less_than(i, self.parent(i)):
            self._bubble_up(i)
        else:
            self.heapify(i)
