from MinHeap import MinHeap, MinHeapNode
from RBT import RBTree, RBNode
import sys

class GatorTaxi:
    def __init__(self):
        # Initialize the instances of RBTree and MinHeap classes
        self.rbtree = RBTree()
        self.min_heap = MinHeap()

    def insert_ride(self, ride_number, ride_cost, trip_duration):
        # Search for the node in RBTree
        rb_node = self.rbtree.search(ride_number)
        if rb_node:
            return "Duplicate RideNumber"

        # Create new nodes for MinHeap and RBTree
        rb_node = RBNode(ride_number, ride_cost, trip_duration)
        min_heap_node = MinHeapNode(ride_number, ride_cost, trip_duration)

        # Assign the pointers to each other for correspondence
        rb_node.min_heap_node = min_heap_node
        min_heap_node.rbt_node = rb_node

        # Insert the nodes into the respective structures
        self.rbtree.insert(rb_node)
        self.min_heap.insert(min_heap_node)

    def print_ride(self, ride_number):
        rb_node = self.rbtree.search(ride_number)
        if rb_node:
            # Return (rideNumber, rideCost, tripDuration) if the node is found
            return f"({rb_node.rideNumber},{rb_node.rideCost},{rb_node.tripDuration})"
        else:
            # Return (0,0,0) if the node is not present
            return "(0,0,0)"

    def print_range(self, node, ride_number1, ride_number2, res):
        # Traverse the Red-Black Tree and append nodes in the range [ride_number1, ride_number2] to res
        if node is None:
            return
        if ride_number1 < node.rideNumber:
            self.print_range(node.left, ride_number1, ride_number2, res)
        if ride_number1 <= node.rideNumber <= ride_number2:
            res.append([node.rideNumber, node.rideCost, node.tripDuration])
        if ride_number2 > node.rideNumber:
            self.print_range(node.right, ride_number1, ride_number2, res)

    def print_rides(self, ride_number1, ride_number2):
        res = []
        self.print_range(self.rbtree.root, ride_number1, ride_number2, res)
        if len(res) == 0:
            # Return (0,0,0) if there are no nodes in the range
            return "(0,0,0)"
        else:
            # Convert each node in res to a string representation and concatenate them
            out_val = ",".join([f"{i[0],i[1],i[2]}".replace(" ", "") for i in res])
            return out_val

    def get_next_ride(self):
        # Extract the minimum cost ride from heap and delete it from the RBTree
        min_heap_node = self.min_heap.extract_min()

        if min_heap_node:
            self.rbtree.delete(min_heap_node.rbt_node.rideNumber)
            out_val = f"({min_heap_node.rideNumber},{min_heap_node.rideCost},{min_heap_node.tripDuration})"
            return out_val
        else:
            return "No active ride requests"

    def cancel_ride(self, ride_number):
        # Search for the node in RBTree
        rb_node = self.rbtree.search(ride_number)
        if not rb_node:
            return

        # Delete the nodes in both the structures corresponding to the cancelled ride
        self.min_heap.delete_node(rb_node.min_heap_node)
        self.rbtree.delete(rb_node.rideNumber)

    def update_trip(self, ride_number, new_trip_duration):
        # Search for the node in RBTree
        rb_node = self.rbtree.search(ride_number)
        if not rb_node:
            return

        if new_trip_duration <= rb_node.tripDuration:
            # Update the new_tripDuration in the RBTree node
            rb_node.tripDuration = new_trip_duration

            # Update the corresponding minheap node
            self.min_heap.update_trip_duration(rb_node.min_heap_node, new_trip_duration)

        elif rb_node.tripDuration < new_trip_duration <= (2 * rb_node.tripDuration):
            # Update the rideCost and tripDuration in the RBTree node
            rb_node.rideCost += 10  # Add a penalty of 10 on rideCost
            rb_node.tripDuration = new_trip_duration

            # Update the corresponding minheap node
            self.min_heap.increase_key(rb_node.min_heap_node, rb_node.rideCost)
            self.min_heap.update_trip_duration(rb_node.min_heap_node, new_trip_duration)

        else:
            # Ride should be declined
            self.cancel_ride(ride_number)


if __name__ == '__main__':
    # Return if the invoked incorrectly without necessary arguments
    if len(sys.argv) < 2:
        print("Usage: python3 <filename.py> <input_file.txt>")
        sys.exit(1)

    # Set input and output files
    input_file = sys.argv[1]
    output_file = "output_file.txt"

    # Create an object of the taxi class
    gator_taxi = GatorTaxi()

    # Define a function to write to file
    def write_to_file(string, fp):
        print(string)
        fp.write(string + '\n')

    # Open the input and output files
    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        # Loop over each line in the input file
        for line in f:
            # Parse the command and arguments from the line
            command = line.strip().split('(')[0]
            args = line.strip().split('(')[1].replace(')', '').split(',')
            
            # Execute the appropriate function based on the command
            if command == 'Insert':
                ride_number = int(args[0])
                ride_cost = int(args[1])
                trip_duration = int(args[2])
                ret_val = gator_taxi.insert_ride(ride_number, ride_cost, trip_duration)
                if ret_val:
                    write_to_file(ret_val, out)
                    break

            elif command == 'Print':
                if len(args) == 1:
                    ride_number = int(args[0])
                    write_to_file(str(gator_taxi.print_ride(ride_number)), out)
                elif len(args) == 2:
                    ride_number1 = int(args[0])
                    ride_number2 = int(args[1])
                    write_to_file(str(gator_taxi.print_rides(ride_number1, ride_number2)), out)

            elif command == 'UpdateTrip':
                ride_number = int(args[0])
                new_trip_duration = int(args[1])
                gator_taxi.update_trip(ride_number, new_trip_duration)

            elif command == 'GetNextRide':
                write_to_file(str(gator_taxi.get_next_ride()), out)

            elif command == 'CancelRide':
                ride_number = int(args[0])
                gator_taxi.cancel_ride(ride_number)

            else:
                print("Invalid command:", command)

    # Go to the end of the file and delete it if it's a new line character
    with open(output_file, "r+") as file:
        file.seek(0, 2)
        file.seek(file.tell() - 1)
        if file.read(1) == '\n':
            file.seek(file.tell() - 1)
            file.truncate()
