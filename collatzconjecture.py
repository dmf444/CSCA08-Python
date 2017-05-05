class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.dividebytwo = left
        self.timesthreeplusone = right

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.timesthreeplusone is not None):
            ret += self.timesthreeplusone._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.dividebytwo is not None):
            ret += self.dividebytwo._str_helper(indentation + "\t") + "\n"
        return ret


def collatz(number: int) -> list:
    if(number == 1):
        return [1]
    else:
        if(number % 2 == 0):
            coll_list = collatz(number / 2)
        else:
            coll_list = collatz((number * 3) + 1)
        coll_list.append(number)
        return coll_list


def tree_contains(initial_node: BTNode, param):
    if(initial_node.dividebytwo is None and initial_node.timesthreeplusone is None):
        return initial_node.value == param
    else:
        current = initial_node.value == param
        divisor = False
        multito = False
        if(initial_node.dividebytwo):
            divisor = tree_contains(initial_node.dividebytwo, param)
        if(initial_node.timesthreeplusone):
            multito = tree_contains(initial_node.timesthreeplusone, param)
        return current or divisor or multito


def tree_get(initial_node: BTNode, param):
    if(initial_node.dividebytwo is None and initial_node.timesthreeplusone is None):
        return initial_node
    else:
        current = None
        if(initial_node.value == param):
            current = initial_node
        elif(initial_node.dividebytwo):
            current = tree_get(initial_node.dividebytwo, param)
        elif(initial_node.timesthreeplusone):
            current = tree_get(initial_node.timesthreeplusone, param)
        return current


def build_collatz_tree(initial_node: BTNode, number):
    coll_numbers = collatz(number)
    new_tree = None
    last_created = None
    for i in range(len(coll_numbers)- 1, -1, -1):
        if(tree_contains(initial_node, coll_numbers[i])):
            if(new_tree is not None):
                node = tree_get(initial_node, coll_numbers[i])
                if(node.value * 2 == last_created.value):
                    node.dividebytwo = new_tree
                else:
                    node.timesthreeplusone = new_tree
            return initial_node
        else:
            if(new_tree == None):
                last_created = BTNode(coll_numbers[i])
                new_tree = last_created
            else:
                new_nodez = BTNode(coll_numbers[i])
                if(last_created.value * 2 == new_nodez.value):
                    last_created.dividebytwo = new_nodez
                    last_created = new_nodez
                else:
                    last_created.timesthreeplusone = new_nodez
                    last_created = new_nodez
    return initial_node

h = build_collatz_tree(BTNode(1), 5)
i = build_collatz_tree(h, 40)
j = build_collatz_tree(i, 3)
k = build_collatz_tree(j, 6)
l = build_collatz_tree(k, 9)
print(h)