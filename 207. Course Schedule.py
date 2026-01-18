# Time: O(v+e) v=> vertices e=> edges
# Space: O(v+e) the highest is the space for hashmap

# Have a hashMap to search a particular edge and know what all (vertices) were dependent on it
# Also an indegree array to know how many dependencies are there to complete for a particular edge/node
# Then create a queue and first add all the edges that have 0 dependencies in it, while maintaining a count variable to know how many courses were completed
# Then loop on while q is not empty and pop edges one by one after poping reduce the count of dependencies of other edges that were dependent on the current edge
# Then check if the subtracted result for dependencies is 0 that means the node has become independent and all the dependable courses have been completed
# In that case increment the count and then add that next set on independent elements in the queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nMap = defaultdict(list)
        indegree = [0] * numCourses

        for dep,ind in prerequisites:
            indegree[dep] += 1
            if ind in nMap:
                nMap[ind].append(dep)
            else:
                nMap[ind] = [dep]

        q = deque()
        count = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                count += 1

        while q:
            curr = q.popleft()
            dependents = nMap[curr]
            for num in dependents:
                indegree[num] -= 1
                if indegree[num] == 0:
                    q.append(num)
                    count += 1

        if count == numCourses:
            return True
        return False