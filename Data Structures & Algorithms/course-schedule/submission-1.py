class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # at first glance, seeing that one thing depends on another but the other thing cannot depend on the first thing
        # makes me think about a graph and how we are checking for cycle detection        

        # need to create the dictionary that will represent the adjacency list
        courseMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courseMap[course].append(pre)
        
        visited = set()
        def dfs(course):
            # when would we return yes course can be completed?
            # if no prereqs, return True
            # if course was already visited, cycle!!
            if course in visited:
                return False
            if not courseMap[course]:
                return True
            visited.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            courseMap[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True





