class Trie:
    class TreeNode:

        def __init__(self, val: str = ''):
            self.next = []
            self.val = val  # store one character

        def haveNext(self, nextVal: str = '') -> bool:
            if len(self.next) == 0:
                return False
            if nextVal == '':
                return True
            for child in self.next:
                if child.val == nextVal:
                    return True
                else:
                    return False

        def getNext(self, nextVal: str):
            for child in self.next:
                if child.val == nextVal:
                    return child

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rootNode = self.TreeNode('')


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            return
        node = self.rootNode
        for i in range(0, len(word)):
            if node.haveNext(word[i]):
                node = self.rootNode.getNext(word[i])
            else:
                newNode = self.TreeNode(word[i])
                node.next.append(newNode)
                node = newNode


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return False
        node = self.rootNode
        for letter in word:
            if node.haveNext(letter):
                node = node.getNext(letter)
            else:
                return False
        if node.haveNext():
            return False
        return True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return True
        node = self.rootNode
        for letter in prefix:
            if node.haveNext(letter):
                node = node.getNext(letter)
            else:
                return False
        return True




# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("Apple")
param_2 = obj.search("Apple")
param_3 = obj.startsWith("App")
param_4 = obj.search("App")
print(param_2, param_3, param_4)