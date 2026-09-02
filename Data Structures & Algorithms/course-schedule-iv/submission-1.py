class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # i want to have a set for each node in topological order, and basically union the sets from incoming edges

        # we dont have to worry about cycles

        adj = {i: [] for i in range(numCourses)}
        # how many incoming edges into vertex
        # aka how many prereqs one has
        # we want to clear all prereqs before processing
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[a].append(b)  # must take a before b
            indegree[b] += 1
        
        # stores the prereqs for each course
        # so if you wonder if a is a prereq for b, search preReqList[b]
        preReqList = [set() for _ in range(numCourses)]

        # start from ones without indegrees, without any prereqs
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                preReqList[neighbor].add(curr) # add current prereq to neighbor
                preReqList[neighbor].update(preReqList[curr])
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        output = []
        for a,b in queries:
            output.append(a in preReqList[b])
        return output
            


        

        


        