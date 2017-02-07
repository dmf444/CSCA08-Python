from CSCA48.ex4.AQueue import AQueue
from CSCA48.ex4.NQueue import NQueue
from CSCA48.ex4.Stack import Stack
from CSCA48.ex4.Queue import Queue
from CSCA48.ex4.Steue import Steue


class BinTreeNode:
    """
    A node in a binary tree.
    """

    def __init__(self, data, left=None, right=None):
        """ (BinTreeNode, str, BinTreeNode, BinTreeNode) -> NoneType

        Initialize a new BinTreeNode with data, left and right children.
        """

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """ (BinTreeNode) -> str

        Return a string representing self.
        """

        return ("BinTreeNode(" + repr(self.data) + ", " +
                repr(self.left) + ", " + repr(self.right) + ")")


def bst_insert(root, value):
    """ (BinTreeNode, str) -> BinTreeNode

    Insert a (possibly duplicate) node whose data is value
    into the BST rooted at root.
    Return the root of the updated BST.
    """

    new_node = BinTreeNode(value)

    # look for parent of new node
    curr = root
    parent = None
    while curr != None:
        parent = curr
        if value < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    # if empty BST
    if parent == None:
        root = new_node
    else:
        # make new node appropriate child of parent
        if value < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
    return root


def traverse(container, root: 'BinTreeNode'):
    result = ""
    container.put(root)
    while(not container.is_empty()):
        next_node = container.get()
        if(next_node is not None):
            result += next_node.data
            container.put(next_node.left)
            container.put(next_node.right)
    return result


def reset_node():
    node = BinTreeNode("C")
    node = bst_insert(node, "O")
    node = bst_insert(node, "M")
    node = bst_insert(node, "P")
    node = bst_insert(node, "U")
    node = bst_insert(node, "T")
    node = bst_insert(node, "E")
    node = bst_insert(node, "R")
    node = bst_insert(node, "S")
    return node

node = reset_node()
file = open("ex4.txt", "w")
stack_result = traverse(Stack(), node)
file.write(stack_result + "\n")

node = reset_node()
queue_result = traverse(Queue(), node)
file.write(queue_result + "\n")

node = reset_node()
aqueue_result = traverse(AQueue(), node)
file.write(aqueue_result + "\n")

node = reset_node()
nqueue_result = traverse(NQueue(), node)
file.write(nqueue_result + "\n")

node = reset_node()
steue_result = traverse(Steue(), node)
file.write(steue_result)

file.close()
