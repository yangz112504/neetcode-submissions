class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereqs are like edges
        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)


        def dfs(course, visited,path):
            if course in path:
                return False
            if course in visited:
                return True
            visited.add(course)
            path.add(course)

            for neighbor in adj[course]:
                if not dfs(neighbor,visited, path):
                    return False
            path.remove(course)
            return True

        # detect cycle
        visited = set()
        for course in range(numCourses):
            if course not in visited:
                path = set()
                if not dfs(course,visited,path):
                    return False
        
        return True


