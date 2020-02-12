class Node():
    """
    Helper Node class for linkedlist
    """
    def __init__(self, data):
        """Initialize the node with given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """String representation of this node"""
        return "Node({!r})".format(self.data)


class LinkedList():

    def __init__(self, iterable=None):
        """
        Initialize the linked list with iterable
        """
        self.head = None
        self.tail = None
        self.size = 0

        # append given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def append(self, item):
        """
        Append the item at the tail of the Linked list
        """
        # create a new node
        new_node = Node(item)
        # if linked list is empty
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        # update the tail regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        Best case running time: O(1) if .tail property is used to access
        the last node. The current implementation performs O(1) time complexity
        """
        # create a new node
        new_node = Node(item)
        # if LL is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            new_node.next = self.head

        # change the head to new node
        self.head = new_node
        self.size += 1

    def length(self):
        """Length of this linked list"""
        return self.size

    def is_empty(self):
        """Returns true if linked list is empty"""
        return self.head is None

    def get_at_index(self, index):
        """Get the item at given index"""
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        curr = self.head
        
        for _ in range(index):
            curr = curr.next
        
        return curr.data


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    # print('Deleting items:')
    # ll.delete('B')
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('A')
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))
    # print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

