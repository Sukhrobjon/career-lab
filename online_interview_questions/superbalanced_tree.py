import unittest


def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    if tree_root is None:
        return True
    # depth
    depths = list()
    min_d, max_d = 0, 0
    nodes_stack = []
    nodes_stack.append((tree_root, 0))

    while len(nodes_stack):
        # unpack the stack
        node, depth = nodes_stack.pop()

        # check if node is leaf
        if not node.left and not node.right:
            
            # check if depth is has been seen
            if depth not in depths:
                depths.append(depth)
                

            # check if there more than 2 different depth
            # or the difference between two leaves are > 1
            if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0]-depths[1] > 1)):
                return False
        # else we need to traverse down the tree                
        else:
            if node.left:
                nodes_stack.append((node.left, depth + 1))
            if node.right:
                nodes_stack.append((node.right, depth + 1))

    return True
        



# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_both_subtrees_superbalanced_two(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        right = tree.insert_right(4)
        left.insert_left(3)
        left_right = left.insert_right(7)
        left_right.insert_right(8)
        right_right = right.insert_right(5)
        right_right_right = right_right.insert_right(6)
        right_right_right.insert_right(9)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_right(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
