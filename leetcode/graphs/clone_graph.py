class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        q, clones = [], {node.val}
