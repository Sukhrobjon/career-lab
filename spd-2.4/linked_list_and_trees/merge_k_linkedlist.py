class Solution():

    def __init__(self):
        pass

    def get_min(self, array):
        """
        Find the minimum item in the array and return the index
        Array contains list of head of each linked list 
        """
        min_head = float('-inf')
        index = 0
        for i, node in enumerate(array):
            if node is not None:
                if node.data < min_head:
                    min_head = node.data
                    index = i
        