#!python
# from stack import LinkedStack
# from queue import LinkedQueue


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.left != None or self.right != None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Running time: O(log(n)) if tree is binary"""

        left_height = 0
        right_height = 0
        # check if root node is a leaf if not it's the only node
        if self.is_leaf():
            return 0

        # Check if left child has a value and if so calculate its height
        if self.left:
            left_height = self.left.height()

        # Check if right child has a value and if so calculate its height
        if self.right:
            right_height = self.right.height()

        # Return one more than the greater of the left height and right height
        # when left and right node is none both left and right height is 0 and
        # function returns 1 and keep icrementing by 1
        return max(left_height, right_height) + 1


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best and worst case running time: O(n) it has to recursively call
        the height method on every node while traversing down trees"""
        # Check if root node has a value and if so calculate its height
        return 0 if self.is_empty() else self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(log n) tree is somewhat balanced
        and it uses binary search
        Worst case running time: O(n) tree is not balanced and is
        linked list"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(log n) tree is somewhat balanced
        and it uses binary search
        Worst case running time: O(n) tree is not balanced and is
        linked list"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(log n) tree is somewhat balanced
        and it uses binary search
        Worst case running time: O(n) tree is not balanced and is
        linked list"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)

        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            parent.left = BinaryTreeNode(item)

        # Check if the given item should be inserted right of parent node
        else:
            parent.right = BinaryTreeNode(item)

        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(log n) b/c every time we check a node
        we eliminate half of the options
        Worst case running time: O(n) if tree is very unbalanced it could
        hold structure of LinkedList"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right

        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(log n) since every time we check a node
        we eliminate half of the options
        Worst case running time: O(n) if tree is very unbalanced it could
        hold structure of LinkedList"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(log n) since every time we check a node
        we eliminate half of the options
        Worst case running time: O(n) if tree is very unbalanced it could
        hold structure of LinkedList"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right

        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            # Hint: Remember to update the parent parameter
            return self._find_parent_node_recursive(item, node.left, node)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            # Hint: Remember to update the parent parameter
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            # item.append is uncalled function
            # self._traverse_in_order_recursive(self.root, items.append)

            self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we are visiting each node
        Memory usage: O(n) when node is visited we are adding new item to list"""

        if(node):
            # Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)
            # Visit this node's data with given function
            visit(node.data)
            # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we are visiting each node
        Memory usage: O(n) creating a stack with number of nodes in the tree"""

        stack = []
        while stack or node:
            if node is not None:
                # push it to stack
                stack.append(node)
                node = node.left
            else:
                # pop top of the stack
                node = stack.pop()
                visit(node.data)
                # move node to the right
                node = node.right

        # while stack:
        #     if(stack[-1].left != None):  # if node has left child
        #         stack.append(stack[-1].left)
        #     else:
        #         node = stack.pop()
        #         visit(node.data)
        #         if len(stack) != 0:
        #             node = stack.pop()
        #             visit(node.data)
        #         if(node.right is not None):
        #             stack.append(node.right)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            # self._traverse_pre_order_recursive(self.root, items.append)
            self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we are visiting each node
        Memory usage: O(n) when node is visited we are adding new item to list"""
        if node is not None:
            visit(node.data)
            self._traverse_pre_order_recursive(node.left, visit)
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we are visiting each node
        Memory usage: O(n) creating a stack with number of nodes in the tree"""

        stack = LinkedStack()
        stack.push(node)
        while not stack.is_empty():
            node = stack.pop()
            visit(node.data)
            if(node.right != None):
                stack.push(node.right)
            if(node.left != None):
                stack.push(node.left)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
            # items = self._traverse_post_order_iterative(self.root)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we are visiting each node
        Memory usage: O(n) when node is visited we are adding new item to list"""

        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # visit the node add to list
            visit(node.data)

    def _traverse_post_order_iterative(self, node):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we are visiting each node
        Memory usage: O(n) creating a stack with number of nodes in the tree"""
        '''
        # Using set and stack 
        stack = Stack()
        stack.push(node)
        visited = set()
        while not stack.is_empty():
            if(stack.peek().left != None and stack.peek().left.data not in visited):
                stack.push(stack.peek().left)
            elif(stack.peek().right != None and stack.peek().right.data not in visited):
                stack.push(stack.peek().right)
            else:
                node = stack.pop()
                visit(node.data)
                visited.add(node.data)'''
        # create a list equal to size of tree
        items = [None] * self.size

        i = self.size  # i is the last node
        stack = LinkedStack()
        # add the root node to stack
        stack.push(node)
        # traverse through stack is empty
        while not stack.is_empty():
            i -= 1
            node = stack.pop()
            # i is the last index and assign it to data at the root
            items[i] = node.data
            # check if node has left child and add to stack if it is
            if(node.left != None):
                stack.push(node.left)
            # check if node has right child and add to stack if it is
            if(node.right != None):
                stack.push(node.right)

        return items

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def practice_level_order(self, node, visit):
        """
        Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we visit n times each node
        Memory usage: O(n) we are creating a queue, and adding each node to it
        """
        queue = [node]
        pass
    
    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we visit n times each node
        Memory usage: O(n) we are creating a queue, and adding each node to it"""

        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            if(node.left != None):
                # Enqueue this node's left child, if it exists
                queue.enqueue(node.left)
            if(node.right != None):
                # Enqueue this node's right child, if it exists
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))
    print('height: {}'.format(tree.height()))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))
    print('height: {}'.format(tree.height()))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    # print('items pre-order:   {}'.format(tree.items_pre_order()))
    # print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
