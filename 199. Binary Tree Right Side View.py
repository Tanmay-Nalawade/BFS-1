# Time: O(n)
# Space: O(n)

# USING BFS

# Do a BFS keeping the size variable
# and when we loop on the elements in a particular level just append the value when it's the last node
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        if root == None:
            return res

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if i == size - 1:
                    res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res
    

# Time: O(n)
# Space:O(h)

# USING DFS

# Pass level as a parameter of recursion and have a list to add in all the elements
# So in the DFS fucntion if the index is there matching the level then update the value and if it's not there then append the value
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,res,0)
        return res
    def helper(self,root,res,level):
        if root == None:
            return
        if level == len(res):
            res.append(root.val)
        else:
            res[level] = root.val
        self.helper(root.left,res,level+1)
        self.helper(root.right,res,level+1)