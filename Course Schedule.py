# TC: O(V + E)
# SC: O( V + E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashmap = defaultdict(list)
        indegree = [0] * numCourses
        
        for i in range(len(prerequisites)):
            hashmap[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]] += 1
        
        print(hashmap)
        print(indegree)
        
        q = deque()
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                
        coursesCompleted = 0
        
        while q:
            node = q.popleft()
            coursesCompleted += 1
            for val in hashmap[node]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    q.append(val)
        
        return coursesCompleted == numCourses
                
                
            
        
        
        