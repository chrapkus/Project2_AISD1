import random
import time
import sys
import csv


# Creates and return list of random elements
root_tree = None
root_AVL = None


def rand_table_creator(table_size):
    random_table = []
    counter = 0

    while counter < table_size:
        k = random.randrange(0,(table_size*10)) # it choose value in range 0 to 4 * table size that is not already in table
        if k not in random_table:
            random_table.append(k)
            counter+=1

    return random_table

def timer(f, A):
    tic = time.perf_counter()
    f(A)
    toc = time.perf_counter()
    return round(toc - tic, 5)


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)
            return self.right.findval(lkpval)
        else:
            return self.data
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def sort_tree(arr1):
    root = None
    print(arr1)
    t = arr1.pop(0)
    print(t)
    root = Node(t)

    for v in arr1:
        root.insert(v)
    global root_tree
    root_tree = root
    root.PrintTree()

    return upgradeheight(root)

def upgradeheight(root):
    if root == None:
        return 0
    else:
        return 1+ max(upgradeheight(root.left), upgradeheight(root.right))




def data_input(begining, step, number_of_steps, height_dict):

    for x in range(begining,(number_of_steps*step) + begining+1, step):

        arr1 = rand_table_creator(x)
        arr2 = arr1

        height_dict["Number_of_elements"].append(x)
        height_dict["BST_height"].append(sort_tree(arr1))

        height_dict["AVL_height"].append(inputAVL(arr2))
        global root_tree
        root_tree.height = 0



class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

            # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

def inputAVL(arr):
    my_tree = AVL_Tree()
    root = None
    root = my_tree.insert(root,arr.pop(0))
    for value in arr:
        root = my_tree.insert(root, value)
    return root.height



def dictcreator():
    data_set_algorithms = {}
    data_set_algorithms["Number_of_elements"] = []
    data_set_algorithms["BST_height"] = []
    data_set_algorithms["AVL_height"] = []
    return data_set_algorithms

if __name__ == '__main__':




    dict1 = dictcreator()


    data_input(5000,5000,15,dict1)
    list  = [dict1]
    SortingMethods = ["Height_compare"]

    for i in range(0, 1):
        My_Dict = list[i]
        zd = zip(*My_Dict.values())
        with open(SortingMethods[i] + ".csv", 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(My_Dict.keys())
            writer.writerows(zd)


















