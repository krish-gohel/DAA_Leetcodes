#####################################################################################################################
# Problem: Serialize and Deserialize Binary Tree
# Solution : Recursive Approach
# Time Complexity : O(n)
# Space Complexity : O(n)
#####################################################################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.pointer = None

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        values = data.split(",")
        self.pointer = 0

        def dfs():
            if values[self.pointer] == "N":
                self.pointer += 1
                return None

            node = TreeNode(int(values[self.pointer]))
            self.pointer += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))