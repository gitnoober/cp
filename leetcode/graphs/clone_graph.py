class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        _q, _clones = [], {node.val}
