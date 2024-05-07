from collections import deque


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.simple_set = set()
        self.lengths = set()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        if "." not in word:
            self.simple_set.add(word)
        self.lengths.add(len(word))
        node.word = True

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.simple_set
        N = len(word)
        if N not in self.lengths:
            return False
        st = deque()
        st.append((0, self.root))
        while st:
            idx, node = st.popleft()
            if idx == N:
                if node.word:
                    return True
                continue
            else:
                if word[idx] == ".":
                    for child in node.children:
                        st.append((idx + 1, node.children[child]))
                else:
                    if word[idx] not in node.children:
                        continue
                    st.append((idx + 1, node.children[word[idx]]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
