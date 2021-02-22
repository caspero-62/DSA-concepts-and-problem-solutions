class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # call recursive insert helper function
        self.bst_insert(self.root, new_val)

    def search(self, find_val):
        # call recursive search helper function
        return self.bst_search(self.root, find_val)
        
    def bst_insert(self, ele, new_val):
        """
            logic is to move to the left if value is less than 
            the element's value and right if otherwise.
            Eventually, we find an empty space and insert the new value where appropriate
        """
        if new_val < ele.value:
            if ele.left == None:
                ele.left = Node(new_val)
            else:
                self.bst_insert(ele.left, new_val)
        else:
            if ele.right == None:
                ele.right = Node(new_val)
            else:
                self.bst_insert(ele.right, new_val)
                
    def bst_search(self, ele, find_val):
        """
            logic is to move to the left if value is less than 
            the element's value and right if otherwise.
            If we get an element's value equal to the one we're looking for,
            we return True, otherwise we return False.
        """
        if ele:
            if find_val == ele.value:
                return True
            elif find_val > ele.value:
                return self.bst_search(ele.right, find_val)
            else:
                return self.bst_search(ele.left, find_val)
                
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))