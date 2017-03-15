class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, given_depth):
        self.d = given_depth
        if(self.left):
            self.left.set_depth(given_depth + 1)
        if(self.right):
            self.right.set_depth(given_depth + 1)

    def leaves_and_internals(self, is_root=False):
        if(self.left is None and self.right is None):
            return ({self.value}, set())
        else:
            a = set()
            if is_root:
                a = {self.value}
            (return_leaves, return_internal) = (set(), a)
            if(self.left):
                (left_leaves, left_internal) = \
                    self.left.leaves_and_internals(True)
                return_leaves.update(left_leaves)
                return_internal.update(left_internal)
            if(self.right):
                (right_leaves, right_int) = self.right.leaves_and_internals(
                    True)
                return_internal.update(right_int)
                return_leaves.update(right_leaves)
        return (return_leaves, return_internal)

    def get_height_and_sum(self):
        if(self.left is None and self.right is None):
            result = 1
            sums = self.value
        else:
            left, right, left_sum, right_sum = 0, 0, 0, 0
            if(self.left is not None):
                (left, left_sum) = self.left.get_height_and_sum()
            if(self.right is not None):
                (right, right_sum) = self.right.get_height_and_sum()
            if(left == right):
                sums = self.value + left_sum + right_sum
                result = left + 1
            elif(left > right):
                result = left + 1
                sums = self.value + left_sum
            else:
                result = right + 1
                sums = self.value + right_sum
        return (result, sums)

    def sum_to_deepest(self):
        (depth, sum_of_deepest) = self.get_height_and_sum()
        return sum_of_deepest


if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9), BTNode(10)), BTNode(6)))
