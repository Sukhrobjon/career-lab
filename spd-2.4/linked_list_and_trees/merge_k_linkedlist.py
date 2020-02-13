from linkedlist import LinkedList


class Solution():

    def __init__(self):
        pass

    def merge_k_list(self, array):
        """
        Merge k sorted linked list into one sorted list
        """
        merged_list = []
        # get the first min head
        min_index = self.get_min(array)
        node = array[min_index]
        # assign it as new head of new linkedlist
        new_head = node
        while True:
            min_index = self.get_min(array)
            # if min index is none then we have merged all nodes
            if min_index is None:
                break
            # get that node
            curr_node = array[min_index]
            merged_list.append(curr_node.data)
            # update the head for this min head
            array[min_index] = curr_node.next
        # new head of merged long linked list

        return new_head, merged_list

    def get_min(self, array):
        """
        Find the minimum item in the array and return the index
        Array contains list of head of each linked list
        """
        # check if all linked list has been merged
        
        merged = False
        for head in array:
            if head is not None:
                merged = True
                break
        # if merged we return none and know there is no head in the array
        if merged:
            return None
        # else find the current min head
        min_head = array[0]
        index = 0
        for i, node in enumerate(array):
            # make sure that list is not None
            if node is not None:
                if node.data < min_head:
                    # update the min head
                    min_head = node.data
                    index = i

        return index


obj = Solution()
number = [2, 3, 1, 9, 10]
min_head = obj.get_min(number)
print(f"Min number: {min_head}")