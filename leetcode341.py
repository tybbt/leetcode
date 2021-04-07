"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.iter = []
        def epochInteger(n: [NestedInteger]):
            for element in n:
                if element.isInteger():
                    self.iter.append(element.getInteger())
                else:
                    nestList = element.getList()
                    epochInteger(nestList)
        epochInteger(nestedList)
        self.length = len(self.iter)
        self.curIndex = 0

    def next(self) -> int:
        self.curIndex += 1
        return self.iter[self.curIndex]

    def hasNext(self) -> bool:
        return self.curIndex < self.length-1
