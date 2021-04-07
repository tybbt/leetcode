class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = []
        for i in range(0, 100):
            self.index.append([])
        self.key = []       # max len(key[i]) == 10^i
        self.length = len(self.key)

    def add(self, key: int) -> bool:
        c = key % 100
        if key in self.index[c]:
            return None
        else:
            self.index[c].append(key)

    def remove(self, key: int) -> bool:
        c = key % 100
        if key in self.index[c]:
            self.index[c].remove(key)
            return True
        else:
            return False


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        c = key % 100
        if key in self.index[c]:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
myHashSet.contains(1)
myHashSet.contains(3)
myHashSet.add(2)
myHashSet.contains(2)
myHashSet.remove(2)
myHashSet.contains(2)

