class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            adj[a].append(b)
        
        order = []

        visited = set()

        def dfs(course, visited, path):
            if course in path:
                return False
            if course in visited:
                return True
            
            visited.add(course)
            path.add(course)
            for neighbor in adj[course]:
                if not dfs(neighbor,visited,path):
                    return False
            path.remove(course)
            order.append(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course,visited,set()):
                    return []
        return order

                
        