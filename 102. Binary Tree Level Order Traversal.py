# Time: O(n)
# Space: O(n/2) as we don't add every element at the same time. 2 doesn't matter hence O(n) 

# WITH BFS

# Have a queue to keep track of the levels and a size variable to track the elements present in a particular level
# Then loop until the size variable poping the elements from the queue and adding it to the subarray
# and then if left or right exist then append it again into the queque
# After the for loop append the subArray into the result
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return res
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            subArr = []
            for i in range(size):
                curr = q.popleft()
                subArr.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(subArr)
        return res
    
# WITH DFS

# Time:O(n)
# Space:O(h)

# Pass in the level as the parameter of the recursion
# have a resultant array to hold the subarrays which will depict a particular level
# If a particular subArray is not there on a particular list then create one 
# and keep on adding in the elements at the particular level in the subArr which is present on the index of the result arr thats similar to the level
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.helper(root,0)
        return self.res
    def helper(self,root,level):
        if root == None:
            return
        if level == len(self.res):
            self.res.append([])
        self.res[level].append(root.val)
        self.helper(root.left,level + 1)
        self.helper(root.right, level + 1)