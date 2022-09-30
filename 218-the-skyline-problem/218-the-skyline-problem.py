class SegmentTreeNode:
    
    def __init__(self, left, right, left_child=None, right_child=None):
        self.left = left
        self.right = right
        self.left_child = left_child
        self.right_child = right_child
        self.value = 0
    
    @classmethod
    def create_node(cls, begin, end, points):
        if begin == end:
            return cls(points[begin], points[begin + 1])
        mid = (begin + end) // 2
        left_child = cls.create_node(begin, mid, points)
        right_child = cls.create_node(mid + 1, end, points)
        return cls(points[begin], points[end + 1], left_child, right_child)
    
    @classmethod
    def create_tree(cls, segments):
        points = []
        for left, right, _ in segments:
            points.append(left)
            points.append(right)
        points = sorted(set(points))
        points.append(float('inf'))
        root = cls.create_node(0, len(points) - 2, points)

        segments.sort(key=lambda s: s[2])
        for left, right, value in segments:
            root.update(left, right, value)
        return root

    def update(self, left, right, value):
        left = max(left, self.left)
        right = min(right, self.right)
        if left >= right:
            return
        if self.left == left and self.right == right:
            self.value = value
        else:
            if self.value is not None:
                self.left_child.value = self.value
                self.right_child.value = self.value
                self.value = None
            self.left_child.update(left, right, value)
            self.right_child.update(left, right, value)
    
    def traverse(self):
        if self.value is None:
            yield from self.left_child.traverse()
            yield from self.right_child.traverse()
        else:
            yield self.left, self.value     

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        tree = SegmentTreeNode.create_tree(buildings)
        skyline = []
        prev_value = 0
        for point, value in tree.traverse():
            if value != prev_value:
                skyline.append([point, value])
            prev_value = value
        return skyline