class TrieNode:
	def __init__(self):
        self.word = True
		self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.chilren[i] = TrieNode()
            node = node.chilren[i]
        node.word = True

    def search(word):
        node = self.root
        for i in word:
            if i not in node.chilren:
                return False
            node = node.chilren[i]
        return True
