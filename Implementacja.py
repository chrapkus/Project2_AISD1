import random
import time
import sys
import csv


# Creates and return list of random elements
root_tree = None
root_list = None


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

    t = arr1.pop(0)

    root = Node(t)

    for v in arr1:
        root.insert(v)
    global root_tree
    root_tree = root




def upgradeheight(root):
    if root == None:
        return 0
    else:
        return 1+ max(upgradeheight(root.left), upgradeheight(root.right))

class Node_linked_list:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def insert1(self, value):
        if self == None or self.data < value:
            return Node_linked_list(value,self)

        else:
            current = self
            while current.next != None and current.next.data > value:
                current = current.next

            new1 = Node_linked_list(value,current.next)
            current.next = new1
            return self

def search_linked_list(arr1):
    for value in arr1:
        global root_list
        root = root_list
        while root.data != value:
            root = root.next

def sort_linked_list(array1):
    root = None
    root = Node_linked_list(array1.pop(0), root)
    for value in array1:
        root = root.insert1(value)
    global root_list
    root_list = root
    return root

def search_tree(arr1):
    for n in arr1:
        root_tree.findval(n)

def delate_list(arr1):
    global root_list
    root = root_list
    while root != None:
        curr = root
        del root
        root = curr.next
    del root

def delate_tree(root):
    if root != None:
        delate_tree(root.left)
        delate_tree(root.right)
        del root

def delate_tree_first_call(arr):
    global root_tree
    delate_tree(root_tree)



def data_input(begining, step, number_of_steps, creation_time_dict, search_time_dict, delate_time_dict):

    for x in range(begining,(number_of_steps*step) + begining+1, step):

        arr1 = rand_table_creator(x)
        arr2 = arr1


        creation_time_dict["Number_of_elements"].append(x)
        creation_time_dict["Linked_list"].append(timer(sort_linked_list, arr1))
        creation_time_dict["Binary_search_tree"].append(timer(sort_tree, arr2))

        search_time_dict["Number_of_elements"].append(x)
        search_time_dict["Linked_list"].append(timer(search_linked_list, arr1))
        search_time_dict["Binary_search_tree"].append(timer(search_tree, arr2))

        delate_time_dict["Number_of_elements"].append(x)
        delate_time_dict["Linked_list"].append(timer(delate_list, arr1))
        delate_time_dict["Binary_search_tree"].append(timer(delate_tree_first_call, arr2))



def dictcreator():
    data_set_algorithms = {}
    data_set_algorithms["Number_of_elements"] = []
    data_set_algorithms["Linked_list"] = []
    data_set_algorithms["Binary_search_tree"] = []
    return data_set_algorithms

if __name__ == '__main__':


    dict1 = dictcreator()
    dict2  = dictcreator()
    dict3 = dictcreator()

    data_input(1000,1000,15,dict1,dict2, dict3)
    list  = [dict1, dict2, dict3]
    SortingMethods = ["Creation_time", "Search_time", "Delate_time"]

    for i in range(0, 3):
        My_Dict = list[i]
        zd = zip(*My_Dict.values())
        with open(SortingMethods[i] + ".csv", 'w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(My_Dict.keys())
            writer.writerows(zd)


















